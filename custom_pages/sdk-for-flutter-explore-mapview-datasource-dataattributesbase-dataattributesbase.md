---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-datasource-dataattributesbase-dataattributesbase"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- DataAttributesBase.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li><a href="../../mapview.datasource/DataAttributesBase-class.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-class</a></li>
<li class="self-crumb">DataAttributesBase factory constructor</li>
</ol>
<div class="self-name">DataAttributesBase</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapview.datasource/DataAttributesBase-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>DataAttributesBase constructor</h1></div>
<section class="multi-line-signature">
DataAttributesBase(<wbr/><ol class="parameter-list"> <li>List&lt;<wbr/>String&gt; getAttributeNamesLambda(), </li>
<li><a href="../../mapview.datasource/DataAttributeValueValueType.html">/sdk-for-flutter-explore-mapview-datasource-dataattributevaluevaluetype</a>? getValueTypeLambda(<ol class="parameter-list single-line"> <li>String</li>
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
<li><a href="../../mapview.datasource/DataAttributeValue-class.html">/sdk-for-flutter-explore-mapview-datasource-dataattributevalue-class</a>? getValueLambda(<ol class="parameter-list single-line"> <li>String</li>
</ol>), </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Interface for a collection of data attributes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
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
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li><a href="../../mapview.datasource/DataAttributesBase-class.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-class</a></li>
<li class="self-crumb">DataAttributesBase factory constructor</li>
</ol>
<h5>DataAttributesBase class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>
