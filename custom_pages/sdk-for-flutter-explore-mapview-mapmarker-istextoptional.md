---
title: "isTextOptional property"
slug: "sdk-for-flutter-explore-mapview-mapmarker-istextoptional"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isTextOptional.html -->


<div>
<h1>isTextOptional property</h1></div>
<section id="getter">

bool
isTextOptional


<p>Determines if the marker can be displayed with icon and without text.
Returns <code>true</code> if the marker allows text to be hidden, <code>false</code> otherwise.
Defaults to <code>false</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isTextOptional;</code></pre>

</section>
<section id="setter">

void
isTextOptional=(bool value)


<p>Determines if the marker can be displayed with icon and without text.
Sets whether the marker is allowed to appear without text.</p>
<p>Controls whenever <code>MapMarker</code> can be shown as icon only when <a href="sdk-for-flutter-explore-mapview-mapmarker-isoverlapallowed">MapMarker.isOverlapAllowed</a>
is <code>false</code>, has no effect otherwise. If <code>false</code> then the <code>MapMarker</code> will not appear
when icon or text are blocked by other labels.
If <code>true</code>, icon will appear even if the text part is blocked by other labels.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isTextOptional(bool value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
