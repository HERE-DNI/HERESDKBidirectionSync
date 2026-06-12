---
title: "setManeuverNotificationTimingOptionsWithTimingProfile abstract method"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-setmaneuvernotificationtimingoptionswithtimingprofile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setManeuverNotificationTimingOptionsWithTimingProfile.html -->


<div>
<h1>setManeuverNotificationTimingOptionsWithTimingProfile abstract method</h1></div>

bool
setManeuverNotificationTimingOptionsWithTimingProfile(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode</a> transportMode, </li>
<li><a href="/sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a> timingProfile, </li>
<li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a> options</li>
</ol>)

      

    

<p>Set timing option values for the combination of transport mode and timing profile.</p>
<ul>
<li>
<p><code>transportMode</code> The transport mode of the timing options.</p>
</li>
<li>
<p><code>timingProfile</code> The timing profile of the timing options.</p>
</li>
<li>
<p><code>options</code> The timing options.</p>
</li>
</ul>
<p>Returns <code>bool</code>. <code>True</code> if set successfully, <code>false</code> when options has invalid value, see <a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a> for
more details about options.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool setManeuverNotificationTimingOptionsWithTimingProfile(TransportMode transportMode, TimingProfile timingProfile, ManeuverNotificationTimingOptions options);</code></pre>

 



</div>
`
}</HTMLBlock>
