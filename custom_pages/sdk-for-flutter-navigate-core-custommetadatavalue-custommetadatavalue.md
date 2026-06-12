---
title: "CustomMetadataValue constructor"
slug: "sdk-for-flutter-navigate-core-custommetadatavalue-custommetadatavalue"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CustomMetadataValue.html -->


<div>
<h1>CustomMetadataValue constructor</h1></div>

CustomMetadataValue(<ol class="parameter-list single-line"> <li>String getTagLambda()</li>
</ol>)
    

<p>Abstract class for storing arbitrary metadata types.</p>
<p>By implementing this abstract class, multiple object types can be stored as
desired, simply by adding fields to the implementation that refer to those
objects and then assigning an instance of the CustomMetadataValue derived class
to a map item.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory CustomMetadataValue(
  String Function() getTagLambda,

) =&gt; CustomMetadataValue$Lambdas(
  getTagLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
