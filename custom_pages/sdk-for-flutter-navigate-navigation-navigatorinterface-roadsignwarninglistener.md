---
title: "roadSignWarningListener property"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- roadSignWarningListener.html -->


<div>
<h1>roadSignWarningListener property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>?
roadSignWarningListener


<p>Object to receive notifications about road signs on the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about road signs on the current road.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RoadSignWarningListener? get roadSignWarningListener;</code></pre>

</section>
<section id="setter">

void
roadSignWarningListener=(<a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>? value)


<p>Object to receive notifications about road signs on the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Sets the listener to receive notifications about road signs on the current road.
<strong>Note:</strong> This <code>RoadSignWarningListener</code> will provide
school zone warnings only in case the speed limit inside the school zone is different than the
default speed limit applicable for cars outside the school zone. For warnings about school zones
regardless of their speed limits, the <code>NavigatorInterface.road_sign_warning_listener</code> should be
used and the <code>RoadSignWarning.type</code> should be checked for value <code>RoadSignType.SCHOOL_ZONE</code>.
The school zone warner is a zone warner, which means that for a school zone there will <em>always</em> be
3 warnings emitted, with the <code>SchoolZoneWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>, <code>DistanceType.REACHED</code></p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set roadSignWarningListener(RoadSignWarningListener? value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
