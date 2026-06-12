---
title: "renderedLast abstract method"
slug: "sdk-for-flutter-explore-mapview-maplayerprioritybuilder-renderedlast"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- renderedLast.html -->


<div>
<h1>renderedLast abstract method</h1></div>

<a href="/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a>
renderedLast()

      

    

<p>Sets the priority as rendered after all layers and categories.</p>
<p>Applies to the layer itself or the
category pointed to by the preceding call to <a href="/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-withcategory">MapLayerPriorityBuilder.withCategory</a>.
Notice that the order of calls to the functions
<code>renderedFirst|Last|Before|After</code>
matters, and that after such a call the builder clears the current category and refers again to
the layer itself. Further, only one priority for each layer and layer category should be set
with these functions since previous priorities would be ingored. For example the priority to
render layer category 'C' after layer 'L' would be overridden by the priority to
render layer category 'C' before layer 'L' when building something like</p>
<p><code>withCategory("C").renderedAfterLayer("L").withCategory("C").renderedBeforeLayer("L")</code></p>
<p>The previously defined and prioritised categories can be used as reference.</p>
<p>Returns <a href="/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a>. This class instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapLayerPriorityBuilder renderedLast();</code></pre>

 



</div>
`
}</HTMLBlock>
