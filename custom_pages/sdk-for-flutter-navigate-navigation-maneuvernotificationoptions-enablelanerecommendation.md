---
title: "enableLaneRecommendation property"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enablelanerecommendation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- enableLaneRecommendation.html -->


<div>
<h1>enableLaneRecommendation property</h1></div>

        
        bool
        enableLaneRecommendation
<div class="features">getter/setter pair</div>


<p>A flag that indicates whether lane recommendation should be used when generating notifications.
In case the flag is enabled, <em>only</em> the notification for the <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.distance</a>
maneuver notification type will contain the lane recommendation. The lane recommandation will replace the
direction information in the notification.
<strong>Example:</strong> 'After 250 meters use the right two lanes and turn right.'.
Defaults to <code>false</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool enableLaneRecommendation;</code></pre>

 



</div>
`
}</HTMLBlock>
