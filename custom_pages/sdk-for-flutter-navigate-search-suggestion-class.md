---
title: "Suggestion class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-suggestion-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/Suggestion-class-sidebar.html">

<div>

# <span class="kind-class">Suggestion</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Suggestion is meant to provide relevant suggestions to partial queries, like "restaur", "starbu", "eiffel".

Represents a relevant response to user queries. Suggestions (please check <a href="sdk-for-flutter-navigate-search-suggestiontype">SuggestionType</a>) are either: Place: <a href="sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.place</a> Query: <a href="sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.chain</a> or <a href="sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.category</a>

With "Place" you get data for a concrete place in the world. With "Query" something to follow-up, a way to perform more focused search.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-suggestion-suggestion">Suggestion</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-suggestion-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-suggestion-href">href</a></span> <span class="signature">→ String?</span>  
Direct URL for precise query. Available only for <a href="sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.chain</a> and <a href="sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.category</a>. This is not supported in offline search. Gets the direct link for Discover query.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-suggestion-id">id</a></span> <span class="signature">→ String?</span>  
The unique id of suggested item. It can be used to query further information. For online search, suggestion of type <a href="sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.place</a> will have Suggestion.id same as Place.id. For offline search, only suggestion of type <a href="sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.chain</a>, will have this property filled with identifier number of an associated chain. For example, the chain ID "8778" corresponds to the chain name "ABC Shop". For other types, <a href="sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.place</a> and <a href="sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.category</a> this property will be null. Gets the suggested item id.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-suggestion-place">place</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-search-place-class">Place</a>?</span>  
The suggested place. Available only for <a href="sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.place</a>. Gets the suggested place item.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-suggestion-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-suggestion-title">title</a></span> <span class="signature">→ String</span>  
The localized title for the suggestion. Gets the localized title for the suggestion.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-suggestion-type">type</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-search-suggestiontype">SuggestionType</a></span>  
Type of the suggestion. Gets the type of suggestion.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-suggestion-gethighlights">getHighlights</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-highlighttype">HighlightType</a></span>, <span class="type-parameter">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-indexrange-class">IndexRange</a></span>\></span></span>\></span></span> </span>  
The text slices matching the input query.

<span class="name"><a href="sdk-for-flutter-navigate-search-suggestion-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-suggestion-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-suggestion-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

