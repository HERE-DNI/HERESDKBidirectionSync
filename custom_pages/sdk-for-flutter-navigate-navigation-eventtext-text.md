---
title: "text property"
slug: "sdk-for-flutter-navigate-navigation-eventtext-text"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- text.html -->


<div>
<h1>text property</h1></div>

        
        String
        text
<div class="features">getter/setter pair</div>


<p>The text notification instruction. The text is formatted and localized as specified via
<a href="sdk-for-flutter-navigate-routing-routetextoptions-class">RouteTextOptions</a>.</p>
<p><strong>Note:</strong> During navigation, the text will be always empty when the <a href="sdk-for-flutter-navigate-routing-maneuver-class">Maneuver</a> is
taken from the <code>Navigator</code> or <code>VisualNavigator</code> instance via the provided index.
The text instruction that can be accessed from the <a href="sdk-for-flutter-navigate-routing-route-class">Route</a> instance is meant
as preview and it is not necessarily matching the more comprehensive maneuver information you
can access during navigation. This information can be enhanced with real-time <code>ManeuverNotifications</code>
texts that can be used for spoken text notifications during a trip.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String text;</code></pre>

 



</div>
`
}</HTMLBlock>
