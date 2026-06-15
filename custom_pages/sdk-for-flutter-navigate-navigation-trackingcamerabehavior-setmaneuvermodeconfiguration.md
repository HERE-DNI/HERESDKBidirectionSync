---
title: "setManeuverModeConfiguration abstract method"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehavior-setmaneuvermodeconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setManeuverModeConfiguration.html -->


<div>
<h1>setManeuverModeConfiguration abstract method</h1></div>

void
setManeuverModeConfiguration(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class">TrackingCameraBehaviorManeuverModeConfiguration</a>? maneuverModeConfiguration</li>
</ol>)

      

    

<p>Sets the configuration for camera behavior near maneuvers.</p>
<p>Defines how the camera reacts to nearby maneuvers when
<a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-ismaneuverdetectionenabled">TrackingCameraBehavior.isManeuverDetectionEnabled</a> is <code>true</code>. When set to <code>null</code>, the camera does
not react to maneuvers. The configuration must contain at least one rule to be valid.
Defaults to <code>null</code>.</p>
<ul>
<li><code>maneuverModeConfiguration</code> The maneuver mode configuration. Invalid configurations are rejected.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setManeuverModeConfiguration(TrackingCameraBehaviorManeuverModeConfiguration? maneuverModeConfiguration);</code></pre>

 



</div>
`
}</HTMLBlock>
