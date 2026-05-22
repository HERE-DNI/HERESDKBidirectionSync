---
title: "Untitled"
slug: "sdk-for-flutter-explore-search-suggestion-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Suggestion-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
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
Suggestions (please check /sdk-for-flutter-explore-search-suggestiontype) are either:
Place: /sdk-for-flutter-explore-search-suggestiontype
Query: /sdk-for-flutter-explore-search-suggestiontype or /sdk-for-flutter-explore-search-suggestiontype</p>
<p>With "Place" you get data for a concrete place in the world.
With "Query" something to follow-up, a way to perform more focused search.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Suggestion">
/sdk-for-flutter-explore-search-suggestion-suggestion()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-search-suggestion-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="href">
/sdk-for-flutter-explore-search-suggestion-href
→ String?
</dt>
<dd>
  Direct URL for precise query.
Available only for /sdk-for-flutter-explore-search-suggestiontype and /sdk-for-flutter-explore-search-suggestiontype.
This is not supported in offline search.
Gets the direct link for Discover query.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-explore-search-suggestion-id
→ String?
</dt>
<dd>
  The unique id of suggested item. It can be used to query further information.
For online search, suggestion of type /sdk-for-flutter-explore-search-suggestiontype
will have Suggestion.id same as Place.id.
For offline search, only suggestion of type /sdk-for-flutter-explore-search-suggestiontype,
will have this property filled with identifier number of an associated chain.
For example, the chain ID "8778" corresponds to the chain name "ABC Shop".
For other types, /sdk-for-flutter-explore-search-suggestiontype and /sdk-for-flutter-explore-search-suggestiontype
this property will be null.
Gets the suggested item id.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="place">
/sdk-for-flutter-explore-search-suggestion-place
→ /sdk-for-flutter-explore-search-place-class?
</dt>
<dd>
  The suggested place.
Available only for /sdk-for-flutter-explore-search-suggestiontype.
Gets the suggested place item.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-search-suggestion-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="title">
/sdk-for-flutter-explore-search-suggestion-title
→ String
</dt>
<dd>
  The localized title for the suggestion.
Gets the localized title for the suggestion.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-explore-search-suggestion-type
→ /sdk-for-flutter-explore-search-suggestiontype
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
/sdk-for-flutter-explore-search-suggestion-gethighlights(<wbr/>)
    → Map&lt;<wbr/>/sdk-for-flutter-explore-search-highlighttype, List&lt;<wbr/>/sdk-for-flutter-explore-search-indexrange-class&gt;&gt;

</dt>
<dd>
  The text slices matching the input query.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-search-suggestion-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-search-suggestion-tostring(<wbr/>)
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
/sdk-for-flutter-explore-search-suggestion-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
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



</div>
`
}</HTMLBlock>
