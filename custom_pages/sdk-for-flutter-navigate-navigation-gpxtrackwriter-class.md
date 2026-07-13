---
title: "GPXTrackWriter class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-gpxtrackwriter-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GPXTrackWriter-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/GPXTrackWriter-class-sidebar.html">

<div>

# <span class="kind-class">GPXTrackWriter</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Writes GPX track points to <a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a>.

The instance of the class should be added as a listener to the `LocationEngine` for GPX track recording. Appends the new location to the back segment of the track whenever the listener is called. The following data (if provided) can be recorded and inserted into the resulting <a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a>: `latitude`, `longitude`, `altitude`, `time`, `bearingInDegrees`, `pitchInDegrees`, `speedInMetersPerSecond`, `horizontalAccuracyInMeters`, `verticalAccuracyInMeters`, `bearingAccuracyInDegrees`, `speedAccuracyInMetersPerSecond` and `locationTechnology`.

Use case examples:

A user wants to create and save a new <a href="sdk-for-flutter-navigate-navigation-gpxdocument-class">GPXDocument</a> with one <a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a>:

- create <a href="sdk-for-flutter-navigate-navigation-gpxtrackwriter-class">GPXTrackWriter</a> and add it as a location listener to `LocationEngine`.
- set user parameters to <a href="sdk-for-flutter-navigate-navigation-gpxtrackwriter-track">GPXTrackWriter.track</a> (e.g. <a href="sdk-for-flutter-navigate-navigation-gpxtrack-name">GPXTrack.name</a> or <a href="sdk-for-flutter-navigate-navigation-gpxtrack-description">GPXTrack.description</a>).
- when writing is completed, create a new <a href="sdk-for-flutter-navigate-navigation-gpxdocument-class">GPXDocument</a> with a list of one <a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a> and save the document via <a href="sdk-for-flutter-navigate-navigation-gpxdocument-save">GPXDocument.save</a>.

A user wants to modify and save <a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a> in the existing <a href="sdk-for-flutter-navigate-navigation-gpxdocument-class">GPXDocument</a>:

- load <a href="sdk-for-flutter-navigate-navigation-gpxdocument-class">GPXDocument</a> from a file by the relevant constructor.
- create <a href="sdk-for-flutter-navigate-navigation-gpxtrackwriter-class">GPXTrackWriter</a> with the required track in the list <a href="sdk-for-flutter-navigate-navigation-gpxdocument-tracks">GPXDocument.tracks</a>, add the created instance as a location listener to `LocationEngine`.
- when writing is completed, save the document via <a href="sdk-for-flutter-navigate-navigation-gpxdocument-save">GPXDocument.save</a>.

The `GPXDocument` including all tracks is saved in the <a href="https://www.topografix.com/gpx.asp">GPX</a> file format. Hence, once saved, it can be easily shared with other applications that understand the GPX file format.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxtrackwriter-gpxtrackwriter">GPXTrackWriter</a></span><span class="signature">()</span>  
Creates a new instance of GPXTrackWriter with an empty track inside.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxtrackwriter-gpxtrackwriter-withtrack">GPXTrackWriter.withTrack</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withTrack-param-track" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a></span> <span class="parameter-name">track</span></span>)</span>  
Creates a new instance of <a href="sdk-for-flutter-navigate-navigation-gpxtrackwriter-class">GPXTrackWriter</a> with <a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxtrackwriter-track">track</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a></span>  
GPX track into which GPX track points are written. Gets the GPX track into which GPX track points are written.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-onlocationupdated">onLocationUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onLocationUpdated-param-location" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">location</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called each time a new location is available.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
