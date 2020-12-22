# FotoSort

Desktop GUI application which main function is to rename JPEG photos and video files by prepending date/time (of taking a photo or video) in front of the original filename. This helps to sort media files chronologically by a filename. Program allows also to modify file date/time information if needed.

![fotosort](https://user-images.githubusercontent.com/24280216/102830282-493b5c00-43e9-11eb-8279-17702ae44881.png)

#### Table of Contents
1) [Motivation](#motivation)
2) [Description](#description)
3) [How it works?](#how-it-works)
4) [Running the application](#running-the-application)
    * [Windows](#windows)
    * [Linux](#linux)
5) [State of work](#state-of-work)

## Motivation
The idea of this application arose while organizing photos from some trip during which the photos were taken by different people with different cameras (mobile phones or standalone cameras). We wanted to display photos chronologically, however when some photos were modified (e.g. rotated, retouched etc.) it was not a good solution to sort them by date. Thus, we decided to prepend the date/time of taking a photo to the original filename. This information is retrieved from JPEG Exif data.

Later, some additional features were added such as renaming video files (based on file Modified property) and also possibility to shift file date/time (Exif for JPEG and file Modified property for videos). The latter is especially useful when a photo has been taken with a standalone camera that had a wrong clock setup. 

## Description
FotoSort is a GUI desktop application designed for Windows (tested on Windows 10) and Linux Debian-based (tested on Ubuntu) operating systems.

It offers the following features:
* rename JPEG photos and video files by prepending date/time information in front of the original filename
  * for JPEG - <b>Exif date/time</b> data is used
  * for video - <b>file Modified property</b> is used
* shift file date/time by provided number of years, months, days, hours, minutes and/or seconds
* set file date/time from the filename (if date/time information present in the filename)
* possibility to change accepted file extensions
* possibility to add the application to the directory contex menu (to load directory files while launching the app) -> available only on Windows OS

## How it works?
First step is adding photo and/or video files that we want to rename or modify date. We can do it either by Drag&Drop (works on both files and directories) or Browse for a directory containing media files (click on <i>File->Choose folder...</i>).

1) <b>RENAME files example:</b>

* Before RENAME:
<table style="width:100%">
   <tr>
      <td><img src=https://user-images.githubusercontent.com/24280216/102766135-f6788a80-437d-11eb-9417-d5368cbb0264.png></td>
      <td><img src=https://user-images.githubusercontent.com/24280216/102766379-55d69a80-437e-11eb-9fda-2ebfea3b996a.png></td>
   </tr>
</table>

* After RENAME:
<table style="width:100%">
   <tr>
      <td><img src=https://user-images.githubusercontent.com/24280216/102768020-c5e62000-4380-11eb-8f73-a4c40cbf002c.png></td>
      <td><img src=https://user-images.githubusercontent.com/24280216/102768095-e1e9c180-4380-11eb-87a7-38fa8aa6950e.png></td>
   </tr>
</table>

2) <b>MODIFY DATE example:</b>
<table style="width:100%">
   <tr>
      <th>Before MODIFY DATE</th>
      <th>After MODIFY DATE</th>
   </tr>
   <tr>
      <td><img src=https://user-images.githubusercontent.com/24280216/102768674-d21ead00-4381-11eb-80e5-e9321085230b.png></td>
      <td><img src=https://user-images.githubusercontent.com/24280216/102768681-d5199d80-4381-11eb-937b-8983b341e751.png></td>
   </tr>
</table>

In above example date/time of loaded files was shifted 1 year ahead. Then if someone wants to reflect this change in the filenames they need to click <i>RENAME</i> button. In case someone wants to come back to the date already included in the filename they can click <i>DATE FROM FILENAME</i> button.

3) <b>SETTINGS</b>
<table style="width:100%">
   <tr>
      <th>File extensions</th>
      <th>Context menu</th>
   </tr>
   <tr>
      <td><img src=https://user-images.githubusercontent.com/24280216/102770232-10b56700-4384-11eb-973a-b57de48aab85.png></td>
      <td><img src=https://user-images.githubusercontent.com/24280216/102770237-1317c100-4384-11eb-9355-5ba6b67ae34c.png></td>
   </tr>
</table>

Application also allows to configure accepted file extensions (default - all 'checked'). On Windows machines we can also add <i>fotosort.exe</i> application to the directory contex menu. In order to use that option we must run the application as administrator becasue the app needs to modify Windows registry.

## Running the application
The application was prepared for Windows and Linux operating systems. It was tested on Windows 10 and should work well also on previous Windows versions. It was also tested on Ubuntu and should work well on all Debian-based Linux systems.

### Windows
Download and un-zip Windows Executable archive (<i>fotosort.zip</i>) provided in <a href="https://github.com/uemk/FotoSort/releases/">releases</a>.
Double-click on stand-alone portable executable file <i>fotosort.exe</i>.

### Linux
   1) Option 1:
   
      * Clone or download FotoSort github respository (or source code archive provided in <a href="https://github.com/uemk/FotoSort/releases/">releases</a>)
      * Install the requirements provided in <i>requirements.txt</i>
      * Then, run in shell: ./fotosort.py (file must have executable rights: chmod a+x fotosort.py) 
   
   2) Option 2 (preferred):
      * Download and un-pack Linux Executable archive (<i>fotosort.tar.gz</i>) provided in <a href="https://github.com/uemk/FotoSort/releases/">releases</a>
      * Run in shell: ./fotosort or alternatively run ./install.sh to make the application seen by the system (to revert this operation ./uninstall.sh should be launched). Then, it is possible to start the app by double-click on Desktop fotosort icon (or by just typing <i>fotosort</i> in the shell)
   

## State of work
First stable version released: <a href="https://github.com/uemk/FotoSort/releases/tag/v1.0.0">FotoSort-v1.0.0</a>.

For the moment there is no plan on further application development.
