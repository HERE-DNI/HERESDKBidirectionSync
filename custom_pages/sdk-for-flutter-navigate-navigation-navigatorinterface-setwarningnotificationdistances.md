---
title: "setWarningNotificationDistances abstract method"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-setwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setWarningNotificationDistances.html -->


<div>
<h1>setWarningNotificationDistances abstract method</h1></div>

bool
setWarningNotificationDistances(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-warningtype">WarningType</a> warningType, </li>
<li><a href="/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a> warningNotificationDistances</li>
</ol>)

      

    

<p>Set the warning notification distances for the specified warning types.</p>
<p><strong>Note:</strong> The warning notification distances are set for most warners.
This method can't be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use <code>NavigatorInterface.school_zone_warning_options</code> instead.
Attempting to set the warning notification distances for the school zone warner using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code>.
Always use <code>SchoolZoneWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the school zone warner regardless of the <code>TimingProfile</code>.
If <code>NavigatorInterface.set_warning_notification_distances</code> could be used, this would allow for different distances to be set for each timing profile, which is undesirable.
Attempting to set the warning notification distances for the traffic merge warner using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code>.
Always use <code>TrafficMergeWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the traffic merge warner regardless of the <code>TimingProfile</code>.
Using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code> to avoid
seting different distances on each timing profile since the traffic merge warning is only applicable on highways.</p>
<ul>
<li>
<p><code>warningType</code> The warning type for which the warning notification distances will be set.</p>
</li>
<li>
<p><code>warningNotificationDistances</code> The warning notification distances to be set for the specified warning types.</p>
</li>
</ul>
<p>Returns <code>bool</code>. <code>True</code> if set successfully, <code>false</code> when the warning_type is <code>WarningType.SCHOOL_ZONE</code> or the options have invalid values,
see <a href="/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a> for more details about warning notification distances.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool setWarningNotificationDistances(WarningType warningType, WarningNotificationDistances warningNotificationDistances);</code></pre>

 



</div>
`
}</HTMLBlock>
