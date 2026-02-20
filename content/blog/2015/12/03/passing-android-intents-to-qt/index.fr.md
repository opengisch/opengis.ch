---
title: 'Passing android Intents to Qt – OPENGIS.ch'
date: 2015-12-03
slug: "passing-android-intents-to-qt"
url: "/fr/2015/12/03/passing-android-intents-to-qt/"
source: "www.opengis.ch/fr/2015/12/03/passing-android-intents-to-qt/index.html"
---
Working on QField I had the necessity of passing values from the QtActivity.java to the Qt cpp world, here how I did it using an Intent that is sent to the QtActivity (the one you should not edit that comes with Qt). For much more information see [this post series](<https://www.kdab.com/qt-android-episode-7/>).  
hopefully this will be helpful to someone.
    
    private void startQtActivity() {
    	String dotqgis2_dir = "Test dotqgis2_dir";
    	String share_dir = "Test share_dir";
    	// forward to startQtActivity and finish QFieldActivity
    	Intent intent = new Intent();
    	intent.setClass(QFieldActivity.this, QtActivity.class);
    	intent.putExtra("DOTQGIS2_DIR", dotqgis2_dir);
            intent.putExtra("SHARE_DIR", share_dir);
    	startActivity(intent);
    	finish();
    }
    
    #include <QAndroidJniObject>
    #include <QtAndroid>
    #include <QDebug>
    #ifdef Q_OS_ANDROID
    QString getExtra(QAndroidJniObject extras, QString extra){
        if(extras.isValid()){
            QAndroidJniObject extra_jni = QAndroidJniObject::fromString(extra);
            extra_jni = extras.callObjectMethod("getString", "(Ljava/lang/String;)Ljava/lang/String;", extra_jni.object<jstring>());
            if (extra_jni.isValid()){
                extra = extra_jni.toString();
                qDebug() << extra;
                return extra;
            }
        }
        return "";
    }
    void getIntentExtras(QStringList intentExtras)
    {
        QAndroidJniObject activity = QtAndroid::androidActivity();
        if (activity.isValid()) {
            qDebug() << "activity";
            QAndroidJniObject intent = activity.callObjectMethod("getIntent", "()Landroid/content/Intent;");
            if (intent.isValid()) {
                qDebug() << "intent: " << intent.toString();
                QAndroidJniObject extras = intent.callObjectMethod("getExtras", "()Landroid/os/Bundle;");
                qDebug() << "extras: " << extras.toString();
                QString extra;
                for (int i = 0; i < intentExtras.size(); ++i){
                    extra = intentExtras.at(i).toLocal8Bit().constData();
                    getExtra(extras, extra);
                }
              }
            }
    }
    QStringList intentExtras;
    intentExtras << "DOTQGIS2_DIR" << "SHARE_DIR";
    getIntentExtras(intentExtras);
    #endif
This is the first version of the cpp code that I wrote, just for reference. The above code is much cleaner
    
    #include <QAndroidJniObject>
    #include <QtAndroid>
    #include <QDebug>
    void getIntent()
    {
    #ifdef Q_OS_ANDROID
        QAndroidJniObject activity = QtAndroid::androidActivity();
        if (activity.isValid()) {
            qDebug() << "activity";
            QAndroidJniObject intent = activity.callObjectMethod("getIntent", "()Landroid/content/Intent;");
            if (intent.isValid()) {
                qDebug() << "intent: " << intent.toString();
                QAndroidJniObject extras = intent.callObjectMethod("getExtras", "()Landroid/os/Bundle;");
                if(extras.isValid()){
                    qDebug() << "extras: " << extras.toString();
                    QAndroidJniObject dotqgis2_dir = QAndroidJniObject::fromString("DOTQGIS2_DIR");
                    QAndroidJniObject share_dir = QAndroidJniObject::fromString("SHARE_DIR");
                    dotqgis2_dir = extras.callObjectMethod("getString", "(Ljava/lang/String;)Ljava/lang/String;", dotqgis2_dir.object<jstring>());
                    share_dir = extras.callObjectMethod("getString", "(Ljava/lang/String;)Ljava/lang/String;", share_dir.object<jstring>());
                    if (dotqgis2_dir.isValid()){
                        qDebug() << dotqgis2_dir.toString();
                    }
                    if (share_dir.isValid()){
                        qDebug() << share_dir.toString();
                    }
                }
              }
            }
    #endif
    }
    
### _Related_
