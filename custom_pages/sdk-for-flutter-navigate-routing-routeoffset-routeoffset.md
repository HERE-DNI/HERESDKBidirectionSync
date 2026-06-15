---
title: "RouteOffset constructor"
slug: "sdk-for-flutter-navigate-routing-routeoffset-routeoffset"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RouteOffset.html -->


<div>
<h1>RouteOffset constructor</h1></div>

RouteOffset(<ol class="parameter-list single-line"> <li>int sectionIndex, </li>
<li>double offsetInMeters</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>sectionIndex</code> Index of the corresponding route <a href="sdk-for-flutter-navigate-routing-section-class">Section</a>. The start of the section indicates the start of the offset.</li>
<li><code>offsetInMeters</code> Offset from the start of the indexed <a href="sdk-for-flutter-navigate-routing-section-class">Section</a> to the specified location along the route.
The maximum possible offset is limited by the length of the section and cannot exceed it.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RouteOffset(this.sectionIndex, this.offsetInMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
