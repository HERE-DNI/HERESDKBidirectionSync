---
title: "isCurrentPositionIncluded property"
slug: "sdk-for-flutter-navigate-navigation-areacamerabehavior-iscurrentpositionincluded"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isCurrentPositionIncluded.html -->


<div>
<h1>isCurrentPositionIncluded property</h1></div>
<section id="getter">

bool
isCurrentPositionIncluded


<p>Include current position in camera view.
Decides if the current position should be added to the set of visible points.
Note that if the current position is in the vicinity of any of the visible points, setting this to
<code>false</code> will not explicitly exclude the current position from the camera view. However if displaying
an area potentially away from the current position, this does need to be explicitly set to <code>false</code>
or it will try to include the current position. Defaults to false.
Gets whether to include the current position.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isCurrentPositionIncluded;</code></pre>

</section>
<section id="setter">

void
isCurrentPositionIncluded=(bool value)


<p>Include current position in camera view.
Decides if the current position should be added to the set of visible points.
Note that if the current position is in the vicinity of any of the visible points, setting this to
<code>false</code> will not explicitly exclude the current position from the camera view. However if displaying
an area potentially away from the current position, this does need to be explicitly set to <code>false</code>
or it will try to include the current position. Defaults to false.
Sets whether to include the current position.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isCurrentPositionIncluded(bool value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
