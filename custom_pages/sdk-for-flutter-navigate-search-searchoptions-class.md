---
title: "SearchOptions class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-searchoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SearchOptions-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/SearchOptions-class-sidebar.html">

<div>

# <span class="kind-class">SearchOptions</span> class

</div>

<div class="section desc markdown">

Encapsulates options that control the behavior of search and suggest operations.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-searchoptions-searchoptions">SearchOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-searchoptions-distributedresults">distributedResults</a></span> <span class="signature">↔ bool</span>  
Indicates if search along the route should produce well-distributed results. It is only supported for:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searchoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searchoptions-highdensityencodingenabled">highDensityEncodingEnabled</a></span> <span class="signature">↔ bool</span>  
Allows enabling high density encoding of relevant parameters. For now, it only affects input parameters of type `GeoCorridor`. Only supported for search in `SearchEngine`, otherwise it is ignored. **Note:** This is a closed-alpha release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a <a href="sdk-for-flutter-navigate-search-searcherror">SearchError.forbidden</a> will be propagated in callbacks.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searchoptions-languagecode">languageCode</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>?</span>  
The preferred language of the result. When unset or unsupported language is chosen, results will be returned in their local language.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searchoptions-maxitems">maxItems</a></span> <span class="signature">↔ int?</span>  
The maximum number of items in the response. It should be in the range \[1, 100\]. When not set, results will be limited to 20. For location search (reverse geocode) by default results limited to 1.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searchoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-searchoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searchoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-searchoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
