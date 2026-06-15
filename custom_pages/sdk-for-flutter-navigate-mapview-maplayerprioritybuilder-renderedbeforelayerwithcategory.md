---
title: "renderedBeforeLayerWithCategory abstract method"
slug: "sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedbeforelayerwithcategory"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- renderedBeforeLayerWithCategory.html -->


<div>
<h1>renderedBeforeLayerWithCategory abstract method</h1></div>

<a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a>
renderedBeforeLayerWithCategory(<ol class="parameter-list single-line"> <li>String referenceLayer, </li>
<li>String referenceCategory</li>
</ol>)

      

    

<p>Sets the priority as rendered before the referenceCategory of the referenceLayer.</p>
<p>Applies to the
layer itself or the category pointed to by the preceding call to
<a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-withcategory">MapLayerPriorityBuilder.withCategory</a>.
Notice that the order of calls to the functions
<code>renderedFirst|Last|Before|After</code>
matters, and that after such a call the builder clears the current category and refers again to
the layer itself. Further, only one priority for each layer and layer category should be set
with these functions since previous priorities would be ingored. For example the priority to
render layer category 'C' after layer 'L' would be overridden by the priority to
render layer category 'C' before layer 'L' when building something like</p>
<p><code>withCategory("C").renderedAfterLayer("L").withCategory("C").renderedBeforeLayer("L")</code></p>
<p>The previously defined and prioritised categories can be used as reference.
If the referenceLayer and/or the referenceCategory do not exist, then the function will set
the priority as rendered before all layers and categories.</p>
<ul>
<li>
<p><code>referenceLayer</code> The beforehand defined layer name which renders directly after the current layer.</p>
</li>
<li>
<p><code>referenceCategory</code> The beforehand defined category name which renders directly after the current layer.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a>. This class instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapLayerPriorityBuilder renderedBeforeLayerWithCategory(String referenceLayer, String referenceCategory);</code></pre>

 



</div>
`
}</HTMLBlock>
