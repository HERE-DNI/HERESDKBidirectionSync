---
title: "IsolineOptions.withEVCarOptions constructor"
slug: "sdk-for-flutter-explore-routing-isolineoptions-isolineoptions-withevcaroptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IsolineOptions.withEVCarOptions.html -->


<div>
<h1>IsolineOptions.withEVCarOptions constructor</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the constructor with RoutingOptions parameter instead.")</li>
</ol>
</div>
IsolineOptions.withEVCarOptions(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a> calculationOptions, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-evcaroptions-class">EVCarOptions</a> evCarOptions</li>
</ol>)
    

<p>Constructs options to calculate isolines from destination or origin,
with preferences for isoline calculation and electric car routing options.</p>
<ul>
<li>
<p><code>calculationOptions</code> The options to be used to calculate this isoline.</p>
</li>
<li>
<p><code>evCarOptions</code> The options that should influence the possible routes within the isoline.
This determines also the transportation type.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the constructor with RoutingOptions parameter instead.")

factory IsolineOptions.withEVCarOptions(IsolineOptionsCalculation calculationOptions, EVCarOptions evCarOptions) =&gt; $prototype.withEVCarOptions(calculationOptions, evCarOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
