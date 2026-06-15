---
title: "toStringShort method"
slug: "sdk-for-flutter-navigate-mapview-heremap-tostringshort"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- toStringShort.html -->


<div>
<h1>toStringShort method</h1></div>

<div>
<ol class="annotation-list">
<li>@override</li>
</ol>
</div>
String
toStringShort()

      <div class="features">inherited</div>


<p>A short, textual description of this widget.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@override
String toStringShort() {
  final String type = objectRuntimeType(this, 'Widget');
  return key == null ? type : '$type-$key';
}</code></pre>

 



</div>
`
}</HTMLBlock>
