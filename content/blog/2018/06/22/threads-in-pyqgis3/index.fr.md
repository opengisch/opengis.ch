---
title: 'Using Threads in PyQGIS3 – OPENGIS.ch'
date: 2018-06-22
slug: "threads-in-pyqgis3"
url: "/fr/2018/06/22/threads-in-pyqgis3/"
source: "www.opengis.ch/fr/2018/06/22/threads-in-pyqgis3/index.html"
---
While porting a plugin to QGIS3 I decided to also move all it’s threading infrastructure to QgsTasks. Here three possible variants to implement this.  
the first uses the static method `QgsTask.fromFunction` and is simpler to use. A great quick solution. If you want need control you can look at the second solution that subclasses QgsTask. In this solution I also show how to create subtasks with interdependencies. The third variant, illustrates how to run a processing algorithm in a separate thread.  
One thing to be very careful about is never to create widgets or alter gui in a task. This is a strict Qt guideline – gui must never be altered outside of the main thread. So your progress dialog must operate on the main thread, connecting to the progress report signals from the task which operates in the background thread. This also applies to « print » statements — these aren’t safe to use from a background thread in QGIS and can cause random crashes. Use the thread safe QgsMessageLog.logMessage() approach instead. Actually you should forget print and always use QgsMessageLog.
## using QgsTask.fromFunction
this is a quick and simple way of running a function in a separate thread. When calling `QgsTask.fromFunction()` you can pass an `on_finished` argument with a callback to be executed at the end of `run`.
    
    import random
    from time import sleep
    
    from qgis.core import (QgsApplication, QgsTask, QgsMessageLog, Qgis)
    
    MESSAGE_CATEGORY = 'My tasks from a function'
    
    
    def run(task, wait_time):
        """a dumb test function
        to break the task raise an exception
        to return a successful result return it. This will be passed together
        with the exception (None in case of success) to the on_finished method
        """
        QgsMessageLog.logMessage('Started task {}'.format(task.description()),
                                 MESSAGE_CATEGORY, Qgis.Info)
        wait_time = wait_time / 100
        total = 0
        iterations = 0
        for i in range(101):
            sleep(wait_time)
            # use task.setProgress to report progress
            task.setProgress(i)
            total += random.randint(0, 100)
            iterations += 1
            # check task.isCanceled() to handle cancellation
            if task.isCanceled():
                stopped(task)
                return None
            # raise exceptions to abort task
            if random.randint(0, 500) == 42:
                raise Exception('bad value!')
        return {
            'total': total, 'iterations': iterations, 'task': task.description()
            }
    
    
    def stopped(task):
        QgsMessageLog.logMessage(
            'Task "{name}" was cancelled'.format(name=task.description()),
            MESSAGE_CATEGORY, Qgis.Info)
    
    
    def completed(exception, result=None):
        """this is called when run is finished. Exception is not None if run
        raises an exception. Result is the return value of run."""
        if exception is None:
            if result is None:
                QgsMessageLog.logMessage(
                    'Completed with no exception and no result ' \
                    '(probably the task was manually canceled by the user)',
                    MESSAGE_CATEGORY, Qgis.Warning)
            else:
                QgsMessageLog.logMessage(
                    'Task {name} completed\n'
                    'Total: {total} ( with {iterations} '
                    'iterations)'.format(
                        name=result['task'],
                        total=result['total'],
                        iterations=result['iterations']),
                    MESSAGE_CATEGORY, Qgis.Info)
        else:
            QgsMessageLog.logMessage("Exception: {}".format(exception),
                                     MESSAGE_CATEGORY, Qgis.Critical)
            raise exception
    
    
    # a bunch of tasks
    task1 = QgsTask.fromFunction(
        'waste cpu 1', run, on_finished=completed, wait_time=4)
    task2 = QgsTask.fromFunction(
        'waste cpu 2', run, on_finished=completed, wait_time=3)
    QgsApplication.taskManager().addTask(task1)
    QgsApplication.taskManager().addTask(task2)
    
## Subclassing QgsTask
this solution gives you the full control over the task behaviour. In this example I also illustrate how to create subtasks dependencies.
    
    import random
    from time import sleep
    
    from qgis.core import (Qgis, QgsApplication, QgsMessageLog, QgsTask)
    
    MESSAGE_CATEGORY = 'My subclass tasks'
    
    
    class MyTask(QgsTask):
        """This shows how to subclass QgsTask"""
    
        def __init__(self, description, duration):
    
            super().__init__(description, QgsTask.CanCancel)
            self.duration = duration
            self.total = 0
            self.iterations = 0
            self.exception = None
    
        def run(self):
            """Here you implement your heavy lifting. This method should
            periodically test for isCancelled() to gracefully abort.
            This method MUST return True or False
            raising exceptions will crash QGIS so we handle them internally and
            raise them in self.finished
            """
            QgsMessageLog.logMessage('Started task "{}"'.format(
                self.description()), MESSAGE_CATEGORY, Qgis.Info)
            wait_time = self.duration / 100
            for i in range(101):
                sleep(wait_time)
                # use setProgress to report progress
                self.setProgress(i)
                self.total += random.randint(0, 100)
                self.iterations += 1
                # check isCanceled() to handle cancellation
                if self.isCanceled():
                    return False
                # simulate exceptions to show how to abort task
                if random.randint(0, 500) == 42:
                    # DO NOT raise Exception('bad value!')
                    # this would crash QGIS
                    self.exception = Exception('bad value!')
                    return False
            return True
    
        def finished(self, result):
            """This method is automatically called when self.run returns.
            result is the return value from self.run.
            This function is automatically called when the task has completed (
            successfully or otherwise). You just implement finished() to do 
            whatever
            follow up stuff should happen after the task is complete. finished is
            always called from the main thread, so it's safe to do GUI
            operations and raise Python exceptions here.
            """
            if result:
                QgsMessageLog.logMessage(
                    'Task "{name}" completed\n' \
                    'Total: {total} ( with {iterations} iterations)'.format(
                        name=self.description(),
                        total=self.total,
                        iterations=self.iterations),
                    MESSAGE_CATEGORY, Qgis.Success)
            else:
                if self.exception is None:
                    QgsMessageLog.logMessage(
                        'Task "{name}" not successful but without exception ' \
                        '(probably the task was manually canceled by the '
                        'user)'.format(
                            name=self.description()),
                        MESSAGE_CATEGORY, Qgis.Warning)
                else:
                    QgsMessageLog.logMessage(
                        'Task "{name}" Exception: {exception}'.format(
                            name=self.description(), exception=self.exception),
                        MESSAGE_CATEGORY, Qgis.Critical)
                    raise self.exception
    
        def cancel(self):
            QgsMessageLog.logMessage(
                'Task "{name}" was cancelled'.format(name=self.description()),
                MESSAGE_CATEGORY, Qgis.Info)
            super().cancel()
    
    
    t1 = MyTask('waste cpu long', 10)
    t2 = MyTask('waste cpu short', 6)
    t3 = MyTask('waste cpu mini', 4)
    st1 = MyTask('waste cpu Subtask 1', 5)
    st2 = MyTask('waste cpu Subtask 2', 2)
    st3 = MyTask('waste cpu Subtask 3', 4)
    t2.addSubTask(st1, [t3, t1])
    t1.addSubTask(st2)
    t1.addSubTask(st3)
    QgsApplication.taskManager().addTask(t1)
    QgsApplication.taskManager().addTask(t2)
    QgsApplication.taskManager().addTask(t3)
    
### NEVER, EVER, EVER use print in the QgsTask outside from finished(). finished() is called on the main event loop
    
    from qgis.core import (QgsApplication, QgsMessageLog, QgsTask)
    
    
    class MyTask(QgsTask):
    
        def __init__(self, description, flags):
            super().__init__(description, flags)
    
        def run(self):
            QgsMessageLog.logMessage('Started task {}'.format(self.description()))
    
            # print('crashandburn')
            return True
    
    
    t1 = MyTask('waste cpu', QgsTask.CanCancel)
    QgsApplication.taskManager().addTask(t1)
    
## Call a Processing algorithm in a separate thread
You can simply execute a processing algorithm in a separate thread thanks to `QgsProcessingAlgRunnerTask`. This class takes a processing algorithm, its parameters, a context and a feedback objects and execute the algorithm. `QgsProcessingAlgRunnerTask` offers an `executed` signal to which you can connect and execute further code. `executed` sends two arguments `bool successful` and `dict results`. If you want to retrieve a memory layer you can pass the context as well by using [`partial` or `lambda`](<https://eli.thegreenplace.net/2011/04/25/passing-extra-arguments-to-pyqt-slot/>).  
If you’re wondering what parameter values you need to specify for an algorithm, and what values are acceptable, try running `processing.algorithmHelp('qgis:randompointsinextent')` in the python console. In QGIS 3.2 you’ll get a detailed list of all the parameter options for the algorithm and a summary of acceptable value types and formats for each. Another nice possibility is to run the algorithm from the gui and check the history after.
    
    from functools import partial
    
    from qgis.core import (
        Qgis, QgsApplication, QgsMessageLog, QgsProcessingAlgRunnerTask,
        QgsProcessingContext, QgsProcessingFeedback, QgsProject,
        )
    
    MESSAGE_CATEGORY = 'My processing tasks'
    
    
    def task_finished(context, successful, results):
        if not successful:
            QgsMessageLog.logMessage('Task finished unsucessfully',
                                     MESSAGE_CATEGORY,
                                     Qgis.Warning)
        output_layer = context.getMapLayer(results['OUTPUT'])
        # because getMapLayer doesn't transfer ownership the layer will be
        # deleted when context goes out of scope and you'll get a crash.
        # takeResultLayer transfers ownership so it's then safe to add it to the
        # project and give the project ownership.
        if output_layer.isValid():
            QgsProject.instance().addMapLayer(
                context.takeResultLayer(output_layer.id()))
    
    
    alg = QgsApplication.processingRegistry().algorithmById(
        'qgis:randompointsinextent')
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()
    params = {
        'EXTENT': '4.63,11.57,44.41,48.78 [EPSG:4326]',
        'MIN_DISTANCE': 0.1,
        'POINTS_NUMBER': 100,
        'TARGET_CRS': 'EPSG:4326',
        'OUTPUT': 'memory:My random points'
        }
    task = QgsProcessingAlgRunnerTask(alg, params, context, feedback)
    task.executed.connect(partial(task_finished, context))
    QgsApplication.taskManager().addTask(task)
    
I hope this post can help you porting your plugins to QGIS3 and again if you need professional help for your plugins, don’t hesitate [to contact us](</contact/index.html>).
### _Related_
