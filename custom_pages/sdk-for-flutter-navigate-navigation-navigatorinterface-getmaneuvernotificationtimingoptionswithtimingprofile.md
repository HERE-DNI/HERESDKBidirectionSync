---
title: "getManeuverNotificationTimingOptionsWithTimingProfile abstract method"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuvernotificationtimingoptionswithtimingprofile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getManeuverNotificationTimingOptionsWithTimingProfile.html -->


<div>
<h1>getManeuverNotificationTimingOptionsWithTimingProfile abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a>
getManeuverNotificationTimingOptionsWithTimingProfile(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode</a> transportMode, </li>
<li><a href="/sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a> timingProfile</li>
</ol>)

      

    

<p>Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.</p>
<p>The return value can be used as the base for configuring maneuver notification timings. Configure the relevant attributes
of this object according to your preferences, and then set it by calling setManeuverNotificationTimingOptions function
for the same combination of transport mode and timing profile.</p>
<ul>
<li>
<p><code>transportMode</code> The transport mode of the timing options.</p>
</li>
<li>
<p><code>timingProfile</code> The timing profile of the timing options.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a>. The timing options with default values.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ManeuverNotificationTimingOptions getManeuverNotificationTimingOptionsWithTimingProfile(TransportMode transportMode, TimingProfile timingProfile);</code></pre>

 



</div>
`
}</HTMLBlock>
