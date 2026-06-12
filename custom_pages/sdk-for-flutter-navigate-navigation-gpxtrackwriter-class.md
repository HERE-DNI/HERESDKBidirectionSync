---
title: "GPXTrackWriter class abstract"
slug: "sdk-for-flutter-navigate-navigation-gpxtrackwriter-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GPXTrackWriter-class.html -->


<div>
<h1>GPXTrackWriter class abstract</h1></div>

<p>Writes GPX track points to <a href="/sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a>.</p>
<p>The instance of the class should be added as a listener to the
<code>LocationEngine</code> for GPX track recording.
Appends the new location to the back segment of the track whenever the listener is called.
The following data (if provided) can be recorded and inserted into the resulting <a href="/sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a>: <code>latitude</code>, <code>longitude</code>, <code>altitude</code>, <code>time</code>, <code>bearingInDegrees</code>, <code>pitchInDegrees</code>, <code>speedInMetersPerSecond</code>, <code>horizontalAccuracyInMeters</code>, <code>verticalAccuracyInMeters</code>, <code>bearingAccuracyInDegrees</code>, <code>speedAccuracyInMetersPerSecond</code> and <code>locationTechnology</code>.</p>
<p>Use case examples:</p>
<p>A user wants to create and save a new <a href="/sdk-for-flutter-navigate-navigation-gpxdocument-class">GPXDocument</a> with one <a href="/sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a>:</p>
<ul>
<li>create <a href="/sdk-for-flutter-navigate-navigation-gpxtrackwriter-class">GPXTrackWriter</a> and add it as a location listener to <code>LocationEngine</code>.</li>
<li>set user parameters to <a href="/sdk-for-flutter-navigate-navigation-gpxtrackwriter-track">GPXTrackWriter.track</a> (e.g. <a href="/sdk-for-flutter-navigate-navigation-gpxtrack-name">GPXTrack.name</a> or <a href="/sdk-for-flutter-navigate-navigation-gpxtrack-description">GPXTrack.description</a>).</li>
<li>when writing is completed, create a new <a href="/sdk-for-flutter-navigate-navigation-gpxdocument-class">GPXDocument</a> with a list of one <a href="/sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a> and save the document via <a href="/sdk-for-flutter-navigate-navigation-gpxdocument-save">GPXDocument.save</a>.</li>
</ul>
<p>A user wants to modify and save <a href="/sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a> in the existing <a href="/sdk-for-flutter-navigate-navigation-gpxdocument-class">GPXDocument</a>:</p>
<ul>
<li>load <a href="/sdk-for-flutter-navigate-navigation-gpxdocument-class">GPXDocument</a> from a file by the relevant constructor.</li>
<li>create <a href="/sdk-for-flutter-navigate-navigation-gpxtrackwriter-class">GPXTrackWriter</a> with the required track in the list <a href="/sdk-for-flutter-navigate-navigation-gpxdocument-tracks">GPXDocument.tracks</a>,
add the created instance as a location listener to <code>LocationEngine</code>.</li>
<li>when writing is completed, save the document via <a href="/sdk-for-flutter-navigate-navigation-gpxdocument-save">GPXDocument.save</a>.</li>
</ul>
<p>The <code>GPXDocument</code> including all tracks is saved in the <a href="https://www.topografix.com/gpx.asp">GPX</a> file format. Hence, once saved, it can be easily shared with other applications that understand the GPX file format.</p>


<ul><li>Implemented types</li></ul>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-gpxtrackwriter-gpxtrackwriter">GPXTrackWriter</a></li><li><a href="/sdk-for-flutter-navigate-navigation-gpxtrackwriter-gpxtrackwriter-withtrack">GPXTrackWriter.withTrack</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-core-locationlistener-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-core-locationlistener-runtimetype">runtimeType</a></li><li><a href="/sdk-for-flutter-navigate-navigation-gpxtrackwriter-track">track</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-core-locationlistener-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-core-locationlistener-onlocationupdated">onLocationUpdated</a></li><li><a href="/sdk-for-flutter-navigate-core-locationlistener-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-core-locationlistener-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
