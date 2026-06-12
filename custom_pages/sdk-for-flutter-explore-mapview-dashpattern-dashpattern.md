---
title: "DashPattern constructor"
slug: "sdk-for-flutter-explore-mapview-dashpattern-dashpattern"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DashPattern.html -->


<div>
<h1>DashPattern constructor</h1></div>

DashPattern(<ol class="parameter-list single-line"> <li>double gapLength, </li>
<li>double dashLength</li>
</ol>)
    

<p>Creates a simple dash pattern in which the lengths of a dash and gap can be different.</p>
<p>This allows for patterns like <code>'  —  —  —  —'</code> or <code>' ——— ——— ———'</code>.</p>
<ul>
<li>
<p><code>gapLength</code> The length of a gap in pixels. Clamped to the range of [1, 500].</p>
</li>
<li>
<p><code>dashLength</code> The length of a dash in pixels. Clamped to the range of [1, 500].</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory DashPattern(double gapLength, double dashLength) =&gt; $prototype.$init(gapLength, dashLength);</code></pre>

 



</div>
`
}</HTMLBlock>
