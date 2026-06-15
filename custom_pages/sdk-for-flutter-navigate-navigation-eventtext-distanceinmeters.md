---
title: "distanceInMeters property"
slug: "sdk-for-flutter-navigate-navigation-eventtext-distanceinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- distanceInMeters.html -->


<div>
<h1>distanceInMeters property</h1></div>

        
        double
        distanceInMeters
<div class="features">getter/setter pair</div>


<p>Distance in meters to the location of the event for which the text notification is given.</p>
<p><strong>Note:</strong> For greater distances, distance in kilometers is rounded to the nearest digit (0.5 or
greater rounds up, else down) to simplify the distance phrase in <code>ManeuverNotifications</code> texts
during navigation. Distance in miles is rounded to the nearest 0.5 step. For example, 3.5 kilometers
are rounded to 4 kilometers and the notification will begin with <code>After 4 kilometers...</code>. However,
3.5 miles are not rounded up and the notification will begin with <code>After three and a half miles...</code>.
Same for 3.7 miles, whereas 3.8 miles are rounded to 4 miles. Note that the measurement units itself
are defined in the <code>UnitSystem</code> class.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double distanceInMeters;</code></pre>

 



</div>
`
}</HTMLBlock>
