---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-suggestion-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- Suggestion-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/Suggestion-class.html#constructors">Constructors</a></li>
<li><a href="search/Suggestion/Suggestion.html">Suggestion</a></li>
<li class="section-title">
<a href="search/Suggestion-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="search/Suggestion/hashCode.html">hashCode</a></li>
<li><a href="search/Suggestion/href.html">href</a></li>
<li><a href="search/Suggestion/id.html">id</a></li>
<li><a href="search/Suggestion/place.html">place</a></li>
<li class="inherited"><a href="search/Suggestion/runtimeType.html">runtimeType</a></li>
<li><a href="search/Suggestion/title.html">title</a></li>
<li><a href="search/Suggestion/type.html">type</a></li>
<li class="section-title"><a href="search/Suggestion-class.html#instance-methods">Methods</a></li>
<li><a href="search/Suggestion/getHighlights.html">getHighlights</a></li>
<li class="inherited"><a href="search/Suggestion/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/Suggestion/toString.html">toString</a></li>
<li class="section-title inherited"><a href="search/Suggestion-class.html#operators">Operators</a></li>
<li class="inherited"><a href="search/Suggestion/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">Suggestion class</li>
</ol>
<div class="self-name">Suggestion</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/Suggestion-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Suggestion class abstract</h1></div>
<section class="desc markdown">
<p>Suggestion is meant to provide relevant suggestions to partial queries, like "restaur", "starbu", "eiffel".</p>
<p>Represents a relevant response to user queries.
Suggestions (please check <a href="../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a>) are either:
Place: <a href="../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a>
Query: <a href="../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a> or <a href="../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a></p>
<p>With "Place" you get data for a concrete place in the world.
With "Query" something to follow-up, a way to perform more focused search.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Suggestion">
<a href="../search/Suggestion/Suggestion.html">/sdk-for-flutter-explore-search-suggestion-suggestion</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../search/Suggestion/hashCode.html">/sdk-for-flutter-explore-search-suggestion-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="href">
<a href="../search/Suggestion/href.html">/sdk-for-flutter-explore-search-suggestion-href</a>
→ String?
</dt>
<dd>
  Direct URL for precise query.
Available only for <a href="../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a> and <a href="../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a>.
This is not supported in offline search.
Gets the direct link for Discover query.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
<a href="../search/Suggestion/id.html">/sdk-for-flutter-explore-search-suggestion-id</a>
→ String?
</dt>
<dd>
  The unique id of suggested item. It can be used to query further information.
For online search, suggestion of type <a href="../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a>
will have Suggestion.id same as Place.id.
For offline search, only suggestion of type <a href="../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a>,
will have this property filled with identifier number of an associated chain.
For example, the chain ID "8778" corresponds to the chain name "ABC Shop".
For other types, <a href="../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a> and <a href="../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a>
this property will be null.
Gets the suggested item id.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="place">
<a href="../search/Suggestion/place.html">/sdk-for-flutter-explore-search-suggestion-place</a>
→ <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a>?
</dt>
<dd>
  The suggested place.
Available only for <a href="../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a>.
Gets the suggested place item.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/Suggestion/runtimeType.html">/sdk-for-flutter-explore-search-suggestion-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="title">
<a href="../search/Suggestion/title.html">/sdk-for-flutter-explore-search-suggestion-title</a>
→ String
</dt>
<dd>
  The localized title for the suggestion.
Gets the localized title for the suggestion.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="type">
<a href="../search/Suggestion/type.html">/sdk-for-flutter-explore-search-suggestion-type</a>
→ <a href="../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a>
</dt>
<dd>
  Type of the suggestion.
Gets the type of suggestion.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="getHighlights">
<a href="../search/Suggestion/getHighlights.html">/sdk-for-flutter-explore-search-suggestion-gethighlights</a>(<wbr/>)
    → Map&lt;<wbr/><a href="../search/HighlightType.html">/sdk-for-flutter-explore-search-highlighttype</a>, List&lt;<wbr/><a href="../search/IndexRange-class.html">/sdk-for-flutter-explore-search-indexrange-class</a>&gt;&gt;

</dt>
<dd>
  The text slices matching the input query.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/Suggestion/noSuchMethod.html">/sdk-for-flutter-explore-search-suggestion-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/Suggestion/toString.html">/sdk-for-flutter-explore-search-suggestion-tostring</a>(<wbr/>)
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
<a href="../search/Suggestion/operator_equals.html">/sdk-for-flutter-explore-search-suggestion-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">Suggestion class</li>
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
</div></div>
</div>
</HTMLBlock>
