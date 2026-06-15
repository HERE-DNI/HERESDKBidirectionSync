---
title: "IsolineOptions.withCarOptions constructor"
slug: "sdk-for-flutter-navigate-routing-isolineoptions-isolineoptions-withcaroptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IsolineOptions.withCarOptions.html -->


<div>
<h1>IsolineOptions.withCarOptions constructor</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the constructor with RoutingOptions parameter instead.")</li>
</ol>
</div>
IsolineOptions.withCarOptions(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a> calculationOptions, </li>
<li><a class="deprecated" href="sdk-for-flutter-navigate-routing-caroptions-class">CarOptions</a> carOptions</li>
</ol>)
    

<p>Constructs options to calculate isolines from destination or origin,
with preferences for isoline calculation and car routing options.</p>
<ul>
<li>
<p><code>calculationOptions</code> The options to be used to calculate this isoline.</p>
</li>
<li>
<p><code>carOptions</code> The options that should influence the possible routes within the isoline.
This determines also the transportation type.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the constructor with RoutingOptions parameter instead.")

factory IsolineOptions.withCarOptions(IsolineOptionsCalculation calculationOptions, CarOptions carOptions) =&gt; $prototype.withCarOptions(calculationOptions, carOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
