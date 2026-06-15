---
title: "enableDoubleNotification property"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enabledoublenotification"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- enableDoubleNotification.html -->


<div>
<h1>enableDoubleNotification property</h1></div>

        
        bool
        enableDoubleNotification
<div class="features">getter/setter pair</div>


<p>A flag that indicates whether combined maneuver notifications should be generated.
Such double notifications can be useful when maneuvers are very close.
<strong>Example:</strong> A combined message: 'After 300 meters turn left and then turn right.'.
This way a user can better anticipate the next-next maneuver.
Note that setting to <code>true</code> will make the notification longer as two maneuvers will be merged into one.
When the next-next maneuver action takes place, the notification will be given as usual.
<strong>Example:</strong> 'Now turn left and then then turn right.' will be followed by 'Now turn right.'.
Defaults to <code>true</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool enableDoubleNotification;</code></pre>

 



</div>
`
}</HTMLBlock>
