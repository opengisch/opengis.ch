---
title: 'Interlis translation – OPENGIS.ch'
date: 2017-12-01
slug: "interlis-translation"
url: "/it/2017/12/01/interlis-translation/"
source: "www.opengis.ch/it/2017/12/01/interlis-translation/index.html"
---
Lately, I have been confronted with the need of translating Interlis files (from French to German) to use queries originally developed for German data. I decided to create an automated convertor for Interlis (version 1) Transfer Format files (.ITF) based on the existing cadastral data model from the Swiss confederation (DM01AVCH).  
The ILI model file conversion has been achieved manually once. This was quite simple since the used model is an extension with little to no difference with respect to the confederation model which already exists in several languages.  
Next was to automate the conversion of the ITF files.  
A program developed by Swisstopo called DM01AVCH_Translator existed to translate confederation model’s ITF files. Originally developed in 2008, the solution is sadly no longer maintained by Swisstopo and was available on Windows only. Moreover it can’t be completely automated since some interaction is required in the GUI and some tweaks in the output file are needed.  
So I decided to develop a dedicated and fully automated solution which I’d like to share since it is easily adaptable to new scenarios and hopefully can avoid troubles to those who are playing with Interlis files!  
You can find this utility, written in Python, called ITF_Translator on <https://github.com/opengisch/ITF_Translator>
# ITF_Translator
ITF_Translator is capable of translating Interlis v1 transfer files (ITF) to another language thanks to a dictionary text file. Currently restricted to German, French and Italian, it is a simple operation to add support for other languages.  
ITFTranslator class from itf_translator_generic module creates a translator object based on a custom dictionary file whereas some custom translations rules can be added.  
Two extensions of ITFTranslator exist already and contain everything needed to translate DM01AVCH (cadastral data model from the Swiss confederation) and MD01MOVD (cadastral data model from Canton Vaud). These classes are ITFTranslatorDM01AVCH respectively ITFTranslatorMD01MOVD.  
![Diagram illustrating the INTERLIS translation workflow between model languages](https://documents.lucidchart.com/documents/d4616523-4323-46c8-b964-a2d408f2051c/pages/0_0?a=204&x=162&y=206&w=1276&h=308&store=1&accept=image%2F*&auth=LCA%2090d759de416ce1d7dc7b7a42bd7f9aa5951828d9-ts%3D1505628781)
## Dictionary file
The dictionary file is a text file composed of line formatted as follows:  
german_translation;french_tranlsation;italian_translation  
with the following rules:
  - line beginning with ‘#’ and blank lines are ignored
  - no spaces are allowed, use underscores ‘_’ instead


Lines are read from the top to the bottom. If a translation key is repeated, the last one will be used.  
The existing dictionaries for ITFTranslatorDM01AVCH and ITFTranslatorMD01MOVD are based on the dictionary from Swisstopo’s tool.
## Usage example
To translate the file input.itf based on the DM01AVCH model from French to German:
    
    translator = ITFTranslatorDM01AVCH('/home/mario/input.itf')
    translator.translate('output.itf', ITFTranslator.LANGUAGE_FR, ITFTranslator.LANGUAGE_DE)
A file named output.itf is created and contains the translation.
## Rules
The ITFTranslatorDM01AVCH and ITFTranslatorMD01MOVD extend ITFTranslator class and implement required additional rules to correctly translate the respective ITF files. These rules exist to handle non reversible translations. For instance in the DM01AVCH model, “element_lineaire” in French can be translated in German to either “linienelement” or “linienobjekt” depending on the topic. Hereby, we have the opportunity to easily add some context dependant rules which could handle any specific use-case.  
Looking at the code ITFTranslatorDM01AVCH demonstrates how easy it is to create translators for other models. Rules are objects of the class SpecialCaseRule
    
    class SpecialCaseRule:
        """Handle non reversible translations"""
        def __init__(self, language_from, language_to, topic, table, translation):
            """Constructor
            :param int language_from:
                the initial language. See the already defined class variables
            :param int language_to:
                the final language. See the already defined class variables
            :param str topic:
                the name of the topic
            :param str table:
                the name of the table
            :param str translation:
                the translation to use
            """
            self.language_from = language_from
            self.language_to = language_to
            self.topic = topic
            self.table = table
            self.translation = translation
    
The goal of these rules is to define the translation of a table within a precise topic. Dictionary based only translations indistinctively treat every occurrence of the words in the source file. The proposed approach is convenient because it combines simple dictionary files which are valid in most cases, and rules to handle specific scenarios.  
An example of a rule defined for ITFTranslatorDM01AVCH is:
    
    SpecialCaseRule(
        ITFTranslator.LANGUAGE_FR, ITFTranslator.LANGUAGE_DE,
        'Bords_de_plan', 'Element_lineaire', 'Linienobjekt')
It solves the example cited previously, specifying that the translation from French to German of the table “Element_lineaire” in the topic “Bords_de_plan” is “Linienobjekt” while the dictionary file says the translation of “Element_lineaire” is “Linienelemen” for any other case.
### _Related_
