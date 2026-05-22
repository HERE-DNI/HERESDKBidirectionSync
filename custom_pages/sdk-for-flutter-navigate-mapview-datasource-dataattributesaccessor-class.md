---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-datasource-dataattributesaccessor-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DataAttributesAccessor-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">DataAttributesAccessor class</li>
</ol>
<div class="self-name">DataAttributesAccessor</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/DataAttributesAccessor-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>DataAttributesAccessor class abstract</h1></div>
<section class="desc markdown">
<p>Accessor used for manipulating data attributes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="DataAttributesAccessor">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesaccessor-dataattributesaccessor()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-runtimetype
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
<dt class="callable" id="addOrReplace">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesaccessor-addorreplace(<wbr/>String name, /sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-class value)
    → void

</dt>
<dd>
  Adds or replaces an attribute.
  

</dd>
<dt class="callable" id="addOrReplaceBoolean">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesaccessor-addorreplaceboolean(<wbr/>String name, bool value)
    → void

</dt>
<dd>
  Adds or replaces a boolean attribute.
  

</dd>
<dt class="callable" id="addOrReplaceColor">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesaccessor-addorreplacecolor(<wbr/>String name, Color value)
    → void

</dt>
<dd>
  Adds or replaces a color attribute.
  

</dd>
<dt class="callable" id="addOrReplaceDouble">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesaccessor-addorreplacedouble(<wbr/>String name, double value)
    → void

</dt>
<dd>
  Adds or replaces a double precision floating decimal attribute.
  

</dd>
<dt class="callable" id="addOrReplaceFloat">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesaccessor-addorreplacefloat(<wbr/>String name, double value)
    → void

</dt>
<dd>
  Adds or replaces a single precision floating decimal attribute.
  

</dd>
<dt class="callable" id="addOrReplaceLong">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesaccessor-addorreplacelong(<wbr/>String name, int value)
    → void

</dt>
<dd>
  Adds or replaces a 64-bits integer attribute.
  

</dd>
<dt class="callable" id="addOrReplaceString">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesaccessor-addorreplacestring(<wbr/>String name, String value)
    → void

</dt>
<dd>
  Adds or replaces a string attribute.
  

</dd>
<dt class="callable inherited" id="getAsString">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getasstring(<wbr/>String name)
    → String?

</dt>
<dd class="inherited">
  Gets the value of an attribute as a string or <code>null</code> if it is not contained.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="getAttributeNames">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getattributenames(<wbr/>)
    → List&lt;<wbr/>String&gt;

</dt>
<dd class="inherited">
  Returns a list of attribute names.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="getBoolean">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getboolean(<wbr/>String name)
    → bool?

</dt>
<dd class="inherited">
  Gets the value of a boolean attribute or <code>null</code> if it is not contained or the type doesn't match.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="getDouble">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getdouble(<wbr/>String name)
    → double?

</dt>
<dd class="inherited">
  Gets the value of a double precision floating decimal attribute or <code>null</code> if it is not contained or the type doesn't match.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="getFloat">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getfloat(<wbr/>String name)
    → double?

</dt>
<dd class="inherited">
  Gets the value of a single precision floating decimal attribute or <code>null</code> if it is not contained or the type doesn't match.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="getInt64">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getint64(<wbr/>String name)
    → int?

</dt>
<dd class="inherited">
  Gets the value of a 64-bits integer attribute or <code>null</code> if it is not contained or the type doesn't match.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="getString">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getstring(<wbr/>String name)
    → String?

</dt>
<dd class="inherited">
  Gets the value of a string attribute or <code>null</code> if it is not contained or the type doesn't match.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="getValue">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getvalue(<wbr/>String name)
    → /sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-class?

</dt>
<dd class="inherited">
  Gets the DataAttributeValue or <code>null</code> if it is not contained.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="getValueType">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-getvaluetype(<wbr/>String name)
    → /sdk-for-flutter-navigate-mapview-datasource-dataattributevaluevaluetype?

</dt>
<dd class="inherited">
  Returns the value type of an attribute or <code>null</code> if it is not contained.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="remove">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesaccessor-remove(<wbr/>String name)
    → void

</dt>
<dd>
  Removes an attribute by name.
  

</dd>
<dt class="callable" id="removeAll">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesaccessor-removeall(<wbr/>)
    → void

</dt>
<dd>
  Removes all attributes.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-datasource-dataattributesbase-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">DataAttributesAccessor class</li>
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



</div>
`
}</HTMLBlock>
