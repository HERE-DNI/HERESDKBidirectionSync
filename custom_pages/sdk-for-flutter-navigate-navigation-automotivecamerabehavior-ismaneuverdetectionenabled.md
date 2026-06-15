---
title: "isManeuverDetectionEnabled property"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-ismaneuverdetectionenabled"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isManeuverDetectionEnabled.html -->


<div>
<h1>isManeuverDetectionEnabled property</h1></div>
<section id="getter">

bool
isManeuverDetectionEnabled


<p>Enables or disables automatic camera adjustments during upcoming maneuvers.
When enabled, the tracking camera automatically adjusts zoom and framing to provide
better visibility of upcoming turns and maneuvers during navigation. The specific
adjustments and their timing are defined in the camera configuration.</p>
<p>If tracking is currently active when this property is changed, the setting takes effect
immediately. Otherwise, it will apply the next time tracking is activated. The initial
state is determined by the camera configuration provided during construction.
Gets whether maneuver-based camera adjustments are enabled.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isManeuverDetectionEnabled;</code></pre>

</section>
<section id="setter">

void
isManeuverDetectionEnabled=(bool value)


<p>Enables or disables automatic camera adjustments during upcoming maneuvers.
When enabled, the tracking camera automatically adjusts zoom and framing to provide
better visibility of upcoming turns and maneuvers during navigation. The specific
adjustments and their timing are defined in the camera configuration.</p>
<p>If tracking is currently active when this property is changed, the setting takes effect
immediately. Otherwise, it will apply the next time tracking is activated. The initial
state is determined by the camera configuration provided during construction.
Sets whether maneuver-based camera adjustments are enabled.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isManeuverDetectionEnabled(bool value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
