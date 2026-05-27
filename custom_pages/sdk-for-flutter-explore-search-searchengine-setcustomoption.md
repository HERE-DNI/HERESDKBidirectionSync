---
title: "Implementation"
slug: "sdk-for-flutter-explore-search-searchengine-setcustomoption"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- setCustomOption.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/SearchEngine-class.html">/sdk-for-flutter-explore-search-searchengine-class</a></li>
<li class="self-crumb">setCustomOption abstract method</li>
</ol>
<div class="self-name">setCustomOption</div>
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
<div class="main-content" data-above-sidebar="search/SearchEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setCustomOption abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a>?
setCustomOption(<wbr/><ol class="parameter-list single-line"> <li>String name, </li>
<li>String value</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets a custom option for search backend queries.</p>
<p>This allows more control over the behavior
of the search algorithm.
Name has the format &lt;endpoint_name&gt;.&lt;option_name&gt;, for example "discover.show".
Values can be combined for the same name by using a comma, for example "truck,fuel".
The custom option is applied only for the endpoint that is specified as prefix in <code>name</code>.
Some of the supported name/value options are:</p>
<ul>
<li>
<p>name = "revgeocode.with", value = "unnamedStreets" enables the retrieval of access points
on unnamed streets.</p>
</li>
<li>
<p>name = "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show", value = "truck"
enables retreival of truck amenities.
<strong>Note:</strong> Only participants of the closed-alpha group can get access from HERE to use this feature,
otherwise, a <a href="../../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a> will be propagated in callbacks.</p>
</li>
<li>
<p>name = "lookup.show" or "discover.show" or "autosuggest.show" or "browse.show", value = "fuel"
enables retreival of fuel station details.
<strong>Note:</strong> Only participants of the closed-alpha group can get access from HERE to use this feature,
otherwise, a <a href="../../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a> will be propagated in callbacks.</p>
</li>
<li>
<p>name = "lookup.show" or "discover.show" or "browse.show", value = "ev"
enables retreival of EV charging station details.</p>
</li>
<li>
<p>name = "lookup.show" or "discover.show" or "browse.show", value = "eMobilityServiceProviders"
enables retreival of e-Mobility Service Providers details.</p>
</li>
<li>
<p>name = "lookup.show" or "discover.show" or "browse.show", value = "tripadvisor"
adds images, ratings, and editorials from Tripadvisor (TM).
<strong>Note:</strong> Only clients with a license with TripAdvisor for rich content will actually get it.
If this licence is missing, TripAdvisor rich content will be missing, with no error reported.
This content is only added to top 10 search results. If more results are returned,
they will be missing rich TripAdvisor content.</p>
</li>
<li>
<p>name = "lookup.datasets" or "discover.datasets" or "browse.datasets" or "autosuggest.datasets",
value = &lt;your_dataset_hrn&gt; enables ingesting and searching of private POIs.
<strong>Note:</strong> Only participants of the search customization can get access from HERE to use this feature,
otherwise, a <a href="../../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a> will be propagated in callbacks.</p>
</li>
<li>
<p>name = "discover.ranking" or "browse.ranking", value = "excursionDistance"
enables balanced distribution of results for search in <code>GeoCorridor</code>.
Constraint: using this parameter when searching an area that is not a <code>GeoCorridor</code> generates
an error <a href="../../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a>.
<strong>Note:</strong> It is recommended to use <a href="../../search/SearchOptions/distributedResults.html">/sdk-for-flutter-explore-search-searchoptions-distributedresults</a> instead.
For a complete list of available endpoints, parameter names and their valid values, refer to
<a href="https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html">HERE Geocoding &amp; Search API v7</a>.
<strong>Note:</strong> It's easy to set a wrong option that makes queries invalid,
so make sure you read and understand the backend documentation.</p>
</li>
<li>
<p><code>name</code> Option name in the format &lt;endpoint_name&gt;.&lt;option_name&gt;, for example "discover.show".</p>
</li>
<li>
<p><code>value</code> Option value.</p>
</li>
</ul>
<p>Returns <a href="../../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a>. Error in case when setting the option fails.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SearchError? setCustomOption(String name, String value);</code></pre>
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
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/SearchEngine-class.html">/sdk-for-flutter-explore-search-searchengine-class</a></li>
<li class="self-crumb">setCustomOption abstract method</li>
</ol>
<h5>SearchEngine class</h5>
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
