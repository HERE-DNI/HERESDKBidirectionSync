---
title: "DataAttributesBase constructor"
slug: "sdk-for-flutter-explore-mapview-datasource-dataattributesbase-dataattributesbase"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DataAttributesBase.html -->


<div>
<h1>DataAttributesBase constructor</h1></div>

DataAttributesBase(<ol class="parameter-list"> <li>List&lt;String&gt; getAttributeNamesLambda(), </li>
<li><a href="/sdk-for-flutter-explore-mapview-datasource-dataattributevaluevaluetype">DataAttributeValueValueType</a>? getValueTypeLambda(<ol class="parameter-list single-line"> <li>String</li>
</ol>), </li>
<li>String? getAsStringLambda(<ol class="parameter-list single-line"> <li>String</li>
</ol>), </li>
<li>String? getStringLambda(<ol class="parameter-list single-line"> <li>String</li>
</ol>), </li>
<li>int? getInt64Lambda(<ol class="parameter-list single-line"> <li>String</li>
</ol>), </li>
<li>double? getFloatLambda(<ol class="parameter-list single-line"> <li>String</li>
</ol>), </li>
<li>double? getDoubleLambda(<ol class="parameter-list single-line"> <li>String</li>
</ol>), </li>
<li>bool? getBooleanLambda(<ol class="parameter-list single-line"> <li>String</li>
</ol>), </li>
<li><a href="/sdk-for-flutter-explore-mapview-datasource-dataattributevalue-class">DataAttributeValue</a>? getValueLambda(<ol class="parameter-list single-line"> <li>String</li>
</ol>), </li>
</ol>)
    

<p>Interface for a collection of data attributes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory DataAttributesBase(
  List&lt;String&gt; Function() getAttributeNamesLambda,
  DataAttributeValueValueType? Function(String) getValueTypeLambda,
  String? Function(String) getAsStringLambda,
  String? Function(String) getStringLambda,
  int? Function(String) getInt64Lambda,
  double? Function(String) getFloatLambda,
  double? Function(String) getDoubleLambda,
  bool? Function(String) getBooleanLambda,
  DataAttributeValue? Function(String) getValueLambda,

) =&gt; DataAttributesBase$Lambdas(
  getAttributeNamesLambda,
  getValueTypeLambda,
  getAsStringLambda,
  getStringLambda,
  getInt64Lambda,
  getFloatLambda,
  getDoubleLambda,
  getBooleanLambda,
  getValueLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
