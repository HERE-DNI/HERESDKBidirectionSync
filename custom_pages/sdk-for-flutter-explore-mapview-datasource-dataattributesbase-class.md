---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-datasource-dataattributesbase-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- DataAttributesBase-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/DataAttributesBase-class.html#constructors">Constructors</a></li>
<li><a href="mapview.datasource/DataAttributesBase/DataAttributesBase.html">DataAttributesBase</a></li>
<li class="section-title inherited">
<a href="mapview.datasource/DataAttributesBase-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview.datasource/DataAttributesBase/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview.datasource/DataAttributesBase/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview.datasource/DataAttributesBase-class.html#instance-methods">Methods</a></li>
<li><a href="mapview.datasource/DataAttributesBase/getAsString.html">getAsString</a></li>
<li><a href="mapview.datasource/DataAttributesBase/getAttributeNames.html">getAttributeNames</a></li>
<li><a href="mapview.datasource/DataAttributesBase/getBoolean.html">getBoolean</a></li>
<li><a href="mapview.datasource/DataAttributesBase/getDouble.html">getDouble</a></li>
<li><a href="mapview.datasource/DataAttributesBase/getFloat.html">getFloat</a></li>
<li><a href="mapview.datasource/DataAttributesBase/getInt64.html">getInt64</a></li>
<li><a href="mapview.datasource/DataAttributesBase/getString.html">getString</a></li>
<li><a href="mapview.datasource/DataAttributesBase/getValue.html">getValue</a></li>
<li><a href="mapview.datasource/DataAttributesBase/getValueType.html">getValueType</a></li>
<li class="inherited"><a href="mapview.datasource/DataAttributesBase/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview.datasource/DataAttributesBase/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview.datasource/DataAttributesBase-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview.datasource/DataAttributesBase/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li class="self-crumb">DataAttributesBase class</li>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/DataAttributesBase-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>DataAttributesBase class abstract</h1></div>
<section class="desc markdown">
<p>Interface for a collection of data attributes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implementers</dt>
<dd><ul class="comma-separated clazz-relationships">
<li><a href="../mapview.datasource/DataAttributes-class.html">/sdk-for-flutter-explore-mapview-datasource-dataattributes-class</a></li>
<li><a href="../mapview.datasource/DataAttributesAccessor-class.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesaccessor-class</a></li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="DataAttributesBase">
<a href="../mapview.datasource/DataAttributesBase/DataAttributesBase.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-dataattributesbase</a>(List&lt;<wbr/>String&gt; getAttributeNamesLambda(), <a href="../mapview.datasource/DataAttributeValueValueType.html">/sdk-for-flutter-explore-mapview-datasource-dataattributevaluevaluetype</a>? getValueTypeLambda(String), String? getAsStringLambda(String), String? getStringLambda(String), int? getInt64Lambda(String), double? getFloatLambda(String), double? getDoubleLambda(String), bool? getBooleanLambda(String), <a href="../mapview.datasource/DataAttributeValue-class.html">/sdk-for-flutter-explore-mapview-datasource-dataattributevalue-class</a>? getValueLambda(String))
</dt>
<dd>
          Interface for a collection of data attributes.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview.datasource/DataAttributesBase/hashCode.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview.datasource/DataAttributesBase/runtimeType.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="getAsString">
<a href="../mapview.datasource/DataAttributesBase/getAsString.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-getasstring</a>(<wbr/>String name)
    → String?

</dt>
<dd>
  Gets the value of an attribute as a string or <code>null</code> if it is not contained.
  

</dd>
<dt class="callable" id="getAttributeNames">
<a href="../mapview.datasource/DataAttributesBase/getAttributeNames.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-getattributenames</a>(<wbr/>)
    → List&lt;<wbr/>String&gt;

</dt>
<dd>
  Returns a list of attribute names.
  

</dd>
<dt class="callable" id="getBoolean">
<a href="../mapview.datasource/DataAttributesBase/getBoolean.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-getboolean</a>(<wbr/>String name)
    → bool?

</dt>
<dd>
  Gets the value of a boolean attribute or <code>null</code> if it is not contained or the type doesn't match.
  

</dd>
<dt class="callable" id="getDouble">
<a href="../mapview.datasource/DataAttributesBase/getDouble.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-getdouble</a>(<wbr/>String name)
    → double?

</dt>
<dd>
  Gets the value of a double precision floating decimal attribute or <code>null</code> if it is not contained or the type doesn't match.
  

</dd>
<dt class="callable" id="getFloat">
<a href="../mapview.datasource/DataAttributesBase/getFloat.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-getfloat</a>(<wbr/>String name)
    → double?

</dt>
<dd>
  Gets the value of a single precision floating decimal attribute or <code>null</code> if it is not contained or the type doesn't match.
  

</dd>
<dt class="callable" id="getInt64">
<a href="../mapview.datasource/DataAttributesBase/getInt64.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-getint64</a>(<wbr/>String name)
    → int?

</dt>
<dd>
  Gets the value of a 64-bits integer attribute or <code>null</code> if it is not contained or the type doesn't match.
  

</dd>
<dt class="callable" id="getString">
<a href="../mapview.datasource/DataAttributesBase/getString.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-getstring</a>(<wbr/>String name)
    → String?

</dt>
<dd>
  Gets the value of a string attribute or <code>null</code> if it is not contained or the type doesn't match.
  

</dd>
<dt class="callable" id="getValue">
<a href="../mapview.datasource/DataAttributesBase/getValue.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-getvalue</a>(<wbr/>String name)
    → <a href="../mapview.datasource/DataAttributeValue-class.html">/sdk-for-flutter-explore-mapview-datasource-dataattributevalue-class</a>?

</dt>
<dd>
  Gets the DataAttributeValue or <code>null</code> if it is not contained.
  

</dd>
<dt class="callable" id="getValueType">
<a href="../mapview.datasource/DataAttributesBase/getValueType.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-getvaluetype</a>(<wbr/>String name)
    → <a href="../mapview.datasource/DataAttributeValueValueType.html">/sdk-for-flutter-explore-mapview-datasource-dataattributevaluevaluetype</a>?

</dt>
<dd>
  Returns the value type of an attribute or <code>null</code> if it is not contained.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview.datasource/DataAttributesBase/noSuchMethod.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview.datasource/DataAttributesBase/toString.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../mapview.datasource/DataAttributesBase/operator_equals.html">/sdk-for-flutter-explore-mapview-datasource-dataattributesbase-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li class="self-crumb">DataAttributesBase class</li>
</ol>
<h5>mapview.datasource library</h5>
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
