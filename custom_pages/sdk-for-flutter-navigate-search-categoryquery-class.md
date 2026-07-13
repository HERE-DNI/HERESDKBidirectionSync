---
title: "CategoryQuery class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-categoryquery-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CategoryQuery-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/CategoryQuery-class-sidebar.html">

<div>

# <span class="kind-class">CategoryQuery</span> class

</div>

<div class="section desc markdown">

The options to specify a query by categories.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-categoryquery-withcategoriesandfilterinarea">CategoryQuery.withCategoriesAndFilterInArea</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withCategoriesAndFilterInArea-param-categories" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a></span>\></span></span> <span class="parameter-name">categories</span>, </span><span id="sdk-for-flutter-navigate-withCategoriesAndFilterInArea-param-filter" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">filter</span>, </span><span id="sdk-for-flutter-navigate-withCategoriesAndFilterInArea-param-area" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-categoryqueryarea-class">CategoryQueryArea</a></span> <span class="parameter-name">area</span></span>)</span>  
Constructs a new instance of this class from provided parameters.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-categoryquery-withcategoriesinarea">CategoryQuery.withCategoriesInArea</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withCategoriesInArea-param-categories" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a></span>\></span></span> <span class="parameter-name">categories</span>, </span><span id="sdk-for-flutter-navigate-withCategoriesInArea-param-area" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-categoryqueryarea-class">CategoryQueryArea</a></span> <span class="parameter-name">area</span></span>)</span>  
Constructs a new instance of this class from provided parameters.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-categoryquery-withcategoryandfilterinarea">CategoryQuery.withCategoryAndFilterInArea</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withCategoryAndFilterInArea-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a></span> <span class="parameter-name">category</span>, </span><span id="sdk-for-flutter-navigate-withCategoryAndFilterInArea-param-filter" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">filter</span>, </span><span id="sdk-for-flutter-navigate-withCategoryAndFilterInArea-param-area" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-categoryqueryarea-class">CategoryQueryArea</a></span> <span class="parameter-name">area</span></span>)</span>  
Constructs a new instance of this class from provided parameters.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-categoryquery-withcategoryinarea">CategoryQuery.withCategoryInArea</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withCategoryInArea-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a></span> <span class="parameter-name">category</span>, </span><span id="sdk-for-flutter-navigate-withCategoryInArea-param-area" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-categoryqueryarea-class">CategoryQueryArea</a></span> <span class="parameter-name">area</span></span>)</span>  
Constructs a new instance of this class from provided parameters.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-area">area</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-search-categoryqueryarea-class">CategoryQueryArea</a></span>  
Area in which to provide the most relevant places.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-categories">categories</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a></span>\></span></span>  
List of categories to be included. A place can be assigned multiple categories. If any of them is in `CategoryQuery.categories`, but none are in `CategoryQuery.excludeCategories`, that place will be included in the response.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-excludecategories">excludeCategories</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a></span>\></span></span>  
List of categories and subcategories to be excluded. A place can be assigned multiple categories. If any of them is in `CategoryQuery.excludeCategories`, that place will not be included in the response, regardless of whether any of its assigned categories have been included in `CategoryQuery.categories`. In short, an exclusion will always win over an inclusion. This is especially useful for excluding specific subcategories from the main category.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-excludechains">excludeChains</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placechain-class">PlaceChain</a></span>\></span></span>  
List of chains to be excluded. A place can be assigned multiple chains. If any of them is in `CategoryQuery.excludeChains`, that place will not be included in the response, regardless of whether any of its assigned chains have been included in `CategoryQuery.includeChains`. In short, an exclusion will always win over an inclusion.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-excludefoodtypes">excludeFoodTypes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placefoodtype-class">PlaceFoodType</a></span>\></span></span>  
List of food types to be excluded. A place can be assigned multiple food types. If any of them is in `CategoryQuery.excludeFoodTypes`, that place will not be included in the response, regardless of whether any of its assigned food types have been included in `CategoryQuery.includeFoodTypes`. In short, an exclusion will always win over an inclusion.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-filter">filter</a></span> <span class="signature">↔ String?</span>  
Full-text filter on POI names/titles. Results with a partial match are included in the response. By default the value is set to null and results will be based on other parameters provided.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-includechains">includeChains</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placechain-class">PlaceChain</a></span>\></span></span>  
List of chains to be included. A place can be assigned multiple chains. If any of them is in `CategoryQuery.includeChains`, but none are in `CategoryQuery.excludeChains`, that place will be included in the response.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-includefoodtypes">includeFoodTypes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placefoodtype-class">PlaceFoodType</a></span>\></span></span>  
List of food types to be included. A place can be assigned multiple food types. If any of them is in `CategoryQuery.includeFoodTypes`, but none are in `CategoryQuery.excludeFoodTypes`, that place will be included in the response.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-placefilter">placeFilter</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-search-placefilter-class">PlaceFilter</a></span>  
The filter options to specify a place in query. Consists of fuel and truck options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-categoryquery-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
