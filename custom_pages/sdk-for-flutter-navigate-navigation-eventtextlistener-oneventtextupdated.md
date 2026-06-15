---
title: "onEventTextUpdated abstract method"
slug: "sdk-for-flutter-navigate-navigation-eventtextlistener-oneventtextupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onEventTextUpdated.html -->


<div>
<h1>onEventTextUpdated abstract method</h1></div>

void
onEventTextUpdated(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-eventtext-class">EventText</a> eventText</li>
</ol>)

      

    

<p>Called whenever there is a new text notification for a maneuver (multiple notifications can be
given for the same maneuver at different distances (for example: "After 500 meters turn
right." or "Now turn right.") and in that case, this method will be called once for each
distance.</p>
<ul>
<li><code>eventText</code> Data related to next text announcement.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onEventTextUpdated(EventText eventText);</code></pre>

 



</div>
`
}</HTMLBlock>
