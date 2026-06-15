---
title: "orientationMode property"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-orientationmode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- orientationMode.html -->


<div>
<h1>orientationMode property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode</a>
orientationMode


<p>The current orientation mode of the camera.
Defines the camera's viewing angle and orientation for tracking mode.
In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.mode2d</a>, the camera looks straight down and rotates with the vehicle heading.
In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.mode3d</a>, the camera is tilted for a perspective view.
In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.modeNorthUp</a>, the camera maintains north-up orientation regardless of vehicle heading.</p>
<p>Changes to this property take effect immediately on the tracking camera and are
preserved when switching between tracking and area modes.
Gets the current orientation mode.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">AutomotiveCameraBehaviorOrientationMode get orientationMode;</code></pre>

</section>
<section id="setter">

void
orientationMode=(<a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode</a> value)


<p>The current orientation mode of the camera.
Defines the camera's viewing angle and orientation for tracking mode.
In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.mode2d</a>, the camera looks straight down and rotates with the vehicle heading.
In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.mode3d</a>, the camera is tilted for a perspective view.
In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.modeNorthUp</a>, the camera maintains north-up orientation regardless of vehicle heading.</p>
<p>Changes to this property take effect immediately on the tracking camera and are
preserved when switching between tracking and area modes.
Sets the orientation mode for the tracking camera.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set orientationMode(AutomotiveCameraBehaviorOrientationMode value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
