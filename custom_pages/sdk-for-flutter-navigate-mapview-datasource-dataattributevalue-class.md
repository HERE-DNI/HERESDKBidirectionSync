---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DataAttributeValue-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">DataAttributeValue class</li>
</ol>
<div class="self-name">DataAttributeValue</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/DataAttributeValue-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>DataAttributeValue class abstract</h1></div>
<section class="desc markdown">
<p>Encapsulates a data attribute value.</p>
<p>Supports basic types and arrays of basic types.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="DataAttributeValue.withArray">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-witharray(List&lt;<wbr/>/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-class&gt; value)
</dt>
<dd>
          Creates an aggregated data attribute value.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="DataAttributeValue.withBoolean">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-withboolean(bool value)
</dt>
<dd>
          Creates a boolean data attribute value.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="DataAttributeValue.withColor">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-withcolor(Color value)
</dt>
<dd>
          Creates a color data attribute value.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="DataAttributeValue.withDouble">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-withdouble(double value)
</dt>
<dd>
          Creates a double precision floating decimal data attribute value.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="DataAttributeValue.withFloat">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-withfloat(double value)
</dt>
<dd>
          Creates a single precision floating decimal data attribute value.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="DataAttributeValue.withInt64">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-withint64(int value)
</dt>
<dd>
          Creates a 64-bit integer data attribute value.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="DataAttributeValue.withString">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-dataattributevalue-withstring(String value)
</dt>
<dd>
          Creates a string data attribute value.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-runtimetype
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
<dt class="callable" id="getArray">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getarray(<wbr/>)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-class&gt;?

</dt>
<dd>
  Gets the array value or <code>null</code> if the type doesn't match.
  

</dd>
<dt class="callable" id="getAsString">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getasstring(<wbr/>)
    → String

</dt>
<dd>
  Returns a string representation of the contained value.
  

</dd>
<dt class="callable" id="getBoolean">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getboolean(<wbr/>)
    → bool?

</dt>
<dd>
  Gets the boolean value or <code>null</code> if the type doesn't match.
  

</dd>
<dt class="callable" id="getColor">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getcolor(<wbr/>)
    → Color?

</dt>
<dd>
  Gets the color value or <code>null</code> if the type doesn't match.
  

</dd>
<dt class="callable" id="getDouble">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getdouble(<wbr/>)
    → double?

</dt>
<dd>
  Gets the double precision floating decimal value or <code>null</code> if the type doesn't match.
  

</dd>
<dt class="callable" id="getFloat">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getfloat(<wbr/>)
    → double?

</dt>
<dd>
  Gets the single precision floating decimal value or <code>null</code> if the type doesn't match.
  

</dd>
<dt class="callable" id="getInt64">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getint64(<wbr/>)
    → int?

</dt>
<dd>
  Gets 64-bits integer value or <code>null</code> if the type doesn't match.
  

</dd>
<dt class="callable" id="getString">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-getstring(<wbr/>)
    → String?

</dt>
<dd>
  Gets the string value or <code>null</code> if the type doesn't match.
  

</dd>
<dt class="callable" id="getType">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-gettype(<wbr/>)
    → /sdk-for-flutter-navigate-mapview-datasource-dataattributevaluevaluetype

</dt>
<dd>
  Returns the type of the value.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-datasource-dataattributevalue-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">DataAttributeValue class</li>
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
