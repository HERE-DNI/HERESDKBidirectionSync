---
title: "withCategory abstract method"
slug: "sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-withcategory"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withCategory.html -->


<div>
<h1>withCategory abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a>
withCategory(<ol class="parameter-list single-line"> <li>String category</li>
</ol>)

      

    

<p>Sets the layer category for which a priority could be defined with the next call to the functions
<code>renderedFirst|Last|BeforeLayer|AfterLayer</code>.</p>
<p>After a priority is defined by calling one of the aforementioned functions, the current category
is cleared and the builder refers again to the layer itself.</p>
<ul>
<li><code>category</code> The name of the layer category.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a>. This class instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapLayerPriorityBuilder withCategory(String category);</code></pre>

 



</div>
`
}</HTMLBlock>
