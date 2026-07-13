---
title: "GPXDocument class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-gpxdocument-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/GPXDocument-class-sidebar.html">

<div>

# <span class="kind-class">GPXDocument</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Use the GPXDocument to load the GPX file.

Only track data is used from the GPX file format (see trkType at <https://www.topografix.com/GPX/1/1/#type_trkType>). Any unknown elements in the file are ignored. Any known element with an invalid value returns an error. Elevation values are ignored.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxdocument-gpxdocument">GPXDocument</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-gpxFilePath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">gpxFilePath</span>, </span><span id="sdk-for-flutter-navigate-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-gpxoptions-class">GPXOptions</a></span> <span class="parameter-name">options</span></span>)</span>  
Create a GPX document from a file.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxdocument-gpxdocument-withtracks">GPXDocument.withTracks</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withTracks-param-tracks" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a></span>\></span></span> <span class="parameter-name">tracks</span></span>)</span>  
Create a GPX document from a list of GPX tracks.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxdocument-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxdocument-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxdocument-tracks">tracks</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a></span>\></span></span>  
The tracks stored in this GPX document. Gets the tracks stored in this GPX document.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxdocument-addtrack">addTrack</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addTrack-param-trackToAdd" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a></span> <span class="parameter-name">trackToAdd</span></span>) <span class="returntype parameter">→ void</span> </span>  
Add track to GPX document.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxdocument-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxdocument-save">save</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-save-param-gpxFilePath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">gpxFilePath</span></span>) <span class="returntype parameter">→ bool</span> </span>  
Saves the document to a file.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxdocument-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxdocument-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxdocument-fromstring">fromString</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-fromString-param-content" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">content</span>, </span><span id="sdk-for-flutter-navigate-fromString-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-gpxoptions-class">GPXOptions</a></span> <span class="parameter-name">options</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-gpxdocument-class">GPXDocument</a></span> </span>  
Create a GPX document from a string.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

