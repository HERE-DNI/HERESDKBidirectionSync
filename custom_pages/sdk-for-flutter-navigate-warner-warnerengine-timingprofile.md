---
title: "timingProfile property"
slug: "sdk-for-flutter-navigate-warner-warnerengine-timingprofile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- timingProfile.html -->


<div>
<h1>timingProfile property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a>
timingProfile


<p>The timing profile that defines when navigation warnings should be triggered.
Configures the base notification thresholds used for delivering
navigation warnings. The effective thresholds depend on the selected
<a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a> and may adjust automatically according to
the current speed limit:</p>
<ul>
<li>For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a>, thresholds apply when the current
speed limit is above 100 km/h (62 mph).</li>
<li>For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a>, thresholds apply when the current
speed limit is above 60 km/h (37 mph).</li>
<li>For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a>, thresholds apply when the current
speed limit is 60 km/h (37 mph) or below.</li>
</ul>
<p><strong>Note:</strong> Custom threshold values can be set, but these timing-profile rules will still apply.
Gets the currently configured <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TimingProfile get timingProfile;</code></pre>

</section>
<section id="setter">

void
timingProfile=(<a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a> value)


<p>The timing profile that defines when navigation warnings should be triggered.
Configures the base notification thresholds used for delivering
navigation warnings. The effective thresholds depend on the selected
<a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a> and may adjust automatically according to
the current speed limit:</p>
<ul>
<li>For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a>, thresholds apply when the current
speed limit is above 100 km/h (62 mph).</li>
<li>For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a>, thresholds apply when the current
speed limit is above 60 km/h (37 mph).</li>
<li>For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a>, thresholds apply when the current
speed limit is 60 km/h (37 mph) or below.</li>
</ul>
<p><strong>Note:</strong> Custom threshold values can be set, but these timing-profile rules will still apply.
Sets the <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a> of the current position.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set timingProfile(TimingProfile value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
