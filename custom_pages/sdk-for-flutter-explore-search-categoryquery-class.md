---
title: "Untitled"
slug: "sdk-for-flutter-explore-search-categoryquery-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CategoryQuery-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">CategoryQuery class</li>
</ol>
<div class="self-name">CategoryQuery</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/CategoryQuery-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>CategoryQuery class</h1></div>
<section class="desc markdown">
<p>The options to specify a query by categories.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="CategoryQuery.withCategoriesAndFilterInArea">
/sdk-for-flutter-explore-search-categoryquery-categoryquery-withcategoriesandfilterinarea(List&lt;<wbr/>/sdk-for-flutter-explore-search-placecategory-class&gt; categories, String filter, /sdk-for-flutter-explore-search-categoryqueryarea-class area)
</dt>
<dd>
          Constructs a new instance of this class from provided parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="CategoryQuery.withCategoriesInArea">
/sdk-for-flutter-explore-search-categoryquery-categoryquery-withcategoriesinarea(List&lt;<wbr/>/sdk-for-flutter-explore-search-placecategory-class&gt; categories, /sdk-for-flutter-explore-search-categoryqueryarea-class area)
</dt>
<dd>
          Constructs a new instance of this class from provided parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="CategoryQuery.withCategoryAndFilterInArea">
/sdk-for-flutter-explore-search-categoryquery-categoryquery-withcategoryandfilterinarea(/sdk-for-flutter-explore-search-placecategory-class category, String filter, /sdk-for-flutter-explore-search-categoryqueryarea-class area)
</dt>
<dd>
          Constructs a new instance of this class from provided parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="CategoryQuery.withCategoryInArea">
/sdk-for-flutter-explore-search-categoryquery-categoryquery-withcategoryinarea(/sdk-for-flutter-explore-search-placecategory-class category, /sdk-for-flutter-explore-search-categoryqueryarea-class area)
</dt>
<dd>
          Constructs a new instance of this class from provided parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="area">
/sdk-for-flutter-explore-search-categoryquery-area
↔ /sdk-for-flutter-explore-search-categoryqueryarea-class
</dt>
<dd>
  Area in which to provide the most relevant places.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="categories">
/sdk-for-flutter-explore-search-categoryquery-categories
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-placecategory-class&gt;
</dt>
<dd>
  List of categories to be included.
A place can be assigned multiple categories. If any of them is in <code>CategoryQuery.categories</code>,
but none are in <code>CategoryQuery.excludeCategories</code>, that place will be included in the response.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="excludeCategories">
/sdk-for-flutter-explore-search-categoryquery-excludecategories
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-placecategory-class&gt;
</dt>
<dd>
  List of categories and subcategories to be excluded.
A place can be assigned multiple categories. If any of them is in <code>CategoryQuery.excludeCategories</code>,
that place will not be included in the response, regardless of whether any of its assigned
categories have been included in <code>CategoryQuery.categories</code>.
In short, an exclusion will always win over an inclusion.
This is especially useful for excluding specific subcategories from the main category.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="excludeChains">
/sdk-for-flutter-explore-search-categoryquery-excludechains
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-placechain-class&gt;
</dt>
<dd>
  List of chains to be excluded.
A place can be assigned multiple chains. If any of them is in <code>CategoryQuery.excludeChains</code>,
that place will not be included in the response, regardless of whether any of its assigned
chains have been included in <code>CategoryQuery.includeChains</code>.
In short, an exclusion will always win over an inclusion.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="excludeFoodTypes">
/sdk-for-flutter-explore-search-categoryquery-excludefoodtypes
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-placefoodtype-class&gt;
</dt>
<dd>
  List of food types to be excluded.
A place can be assigned multiple food types. If any of them is in <code>CategoryQuery.excludeFoodTypes</code>,
that place will not be included in the response, regardless of whether any of its assigned
food types have been included in <code>CategoryQuery.includeFoodTypes</code>.
In short, an exclusion will always win over an inclusion.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="filter">
/sdk-for-flutter-explore-search-categoryquery-filter
↔ String?
</dt>
<dd>
  Full-text filter on POI names/titles.
Results with a partial match are included in the response.
By default the value is set to null
and results will be based on other parameters provided.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-search-categoryquery-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="includeChains">
/sdk-for-flutter-explore-search-categoryquery-includechains
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-placechain-class&gt;
</dt>
<dd>
  List of chains to be included.
A place can be assigned multiple chains. If any of them is in <code>CategoryQuery.includeChains</code>,
but none are in <code>CategoryQuery.excludeChains</code>, that place will be included in the response.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="includeFoodTypes">
/sdk-for-flutter-explore-search-categoryquery-includefoodtypes
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-placefoodtype-class&gt;
</dt>
<dd>
  List of food types to be included.
A place can be assigned multiple food types. If any of them is in <code>CategoryQuery.includeFoodTypes</code>,
but none are in <code>CategoryQuery.excludeFoodTypes</code>, that place will be included in the response.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="placeFilter">
/sdk-for-flutter-explore-search-categoryquery-placefilter
↔ /sdk-for-flutter-explore-search-placefilter-class
</dt>
<dd>
  The filter options to specify a place in query.
Consists of fuel and truck options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-search-categoryquery-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-search-categoryquery-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-search-categoryquery-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-explore-search-categoryquery-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">CategoryQuery class</li>
</ol>
<h5>search library</h5>
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
