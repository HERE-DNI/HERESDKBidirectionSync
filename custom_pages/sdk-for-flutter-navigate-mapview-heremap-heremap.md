---
title: "HereMap constructor"
slug: "sdk-for-flutter-navigate-mapview-heremap-heremap"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- HereMap.html -->


<div>
<h1>HereMap constructor</h1></div>

      const
      HereMap({<ol class="parameter-list"> <li>Key? key, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-heremapcreatedcallback">HereMapCreatedCallback</a>? onMapCreated, </li>
<li>Set&lt;Factory&lt;OneSequenceGestureRecognizer&gt;&gt;? gestureRecognizers, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-nativeviewmode">NativeViewMode</a> mode = NativeViewMode.virtualDisplay, </li>
<li>dynamic options, </li>
</ol>})
    

<p>Creates a widget that displays a map.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">const HereMap({
  Key? key,
  this.onMapCreated,
  this.gestureRecognizers,
  this.mode = NativeViewMode.virtualDisplay,
  options,
})  : this._options = options,
      super(key: key);</code></pre>

 



</div>
`
}</HTMLBlock>
