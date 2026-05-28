---
title: "SpatialNotificationDetails constructor"
slug: "sdk-for-flutter-navigate-navigation-spatialnotificationdetails-spatialnotificationdetails"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SpatialNotificationDetails.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-spatialnotificationdetails-class</li>
<li class="self-crumb">SpatialNotificationDetails constructor</li>
</ol>
<div class="self-name">SpatialNotificationDetails</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="navigation/SpatialNotificationDetails-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>SpatialNotificationDetails constructor</h1></div>
<section class="multi-line-signature">
SpatialNotificationDetails(<wbr/><ol class="parameter-list single-line"> <li>double initialAzimuthInDegrees, </li>
<li>/sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-class audioCuePanning, </li>
<li>Duration estimatedAudioCueDuration</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>initialAzimuthInDegrees</code> Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as
"Turn right on" (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc trajectory
from the front to the right, mimicking the maneuver geometry.
In this case, it is good practice to start the trajectory from an initial azimuth that is located
slightly on the opposite direction of the maneuver (e.g. slightly starting from "front-left")
and terminate the trajectory fully on the right side. The initial azimuth angle of such
a trajectory would be, for example, -5.0 (slightly front-left).
This azimuth value is needed to set the position of the audio renderer before starting to play
the audio cue to avoid unwanted audio "jumps".
The orientation in space for /sdk-for-flutter-navigate-navigation-spatialnotificationdetails-initialazimuthindegrees can be represented by the
following angular values:</li>
</ul>
<table>
<thead>
<tr>
<th align="center">Front</th>
<th align="center">Right</th>
<th align="center">Rear</th>
<th align="center">Left</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">0°</td>
<td align="center">+90°</td>
<td align="center">+- 180</td>
<td align="center">-90°</td>
</tr>
</tbody>
</table>
<ul>
<li><code>audioCuePanning</code> Object to start the angular panning when spatialization of the text notification is desired</li>
<li><code>estimatedAudioCueDuration</code> Estimation of the required time to play an audio cue at speech rate 1.0.
For example the cue "Turn right on Name-Of-A-Street" will playback over an X number of milliseconds.
Therefore, an estimation of this audio cue duration is needed to correctly sync the movement
of sound to the cue (so that audio movement and audio duration match).</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SpatialNotificationDetails(this.initialAzimuthInDegrees, this.audioCuePanning, this.estimatedAudioCueDuration);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-spatialnotificationdetails-class</li>
<li class="self-crumb">SpatialNotificationDetails constructor</li>
</ol>
<h5>SpatialNotificationDetails class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
