---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-tollfare-tollfare"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TollFare.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-tollfare-class</li>
<li class="self-crumb">TollFare constructor</li>
</ol>
<div class="self-name">TollFare</div>
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
<div class="main-content" data-above-sidebar="routing/TollFare-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>TollFare constructor</h1></div>
<section class="multi-line-signature">
TollFare(<wbr/><ol class="parameter-list"> <li>String currency, </li>
<li>double price, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-paymentmethod&gt; paymentMethods, [</li>
<li>/sdk-for-flutter-navigate-core-timerule-class? timeRule = null, </li>
<li>List&lt;<wbr/>String&gt; transponders = const [], </li>
<li>/sdk-for-flutter-navigate-routing-tollfarepass-class? pass = null, </li>
</ol>])
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>currency</code> The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".</li>
<li><code>price</code> The amount of the toll be paid.</li>
<li><code>paymentMethods</code> The list of accepted payment methods like cash and credit card.</li>
<li><code>timeRule</code> The time domain when this fare is valid.
If this field is missing, it means the fare is always valid.
For a detailed description of the Time Domain specification and usage in routing services, please refer to
the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a></li>
<li><code>transponders</code> The list of available transponders.</li>
<li><code>pass</code> Specifies whether this /sdk-for-flutter-navigate-routing-tollfare-class is a multi-travel pass, and its characteristics.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TollFare(String currency, double price, List&lt;PaymentMethod&gt; paymentMethods, [TimeRule? timeRule = null, List&lt;String&gt; transponders = const [], TollFarePass? pass = null])
  : currency = currency, price = price, paymentMethods = paymentMethods, timeRule = timeRule, transponders = transponders, pass = pass ?? null;</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-tollfare-class</li>
<li class="self-crumb">TollFare constructor</li>
</ol>
<h5>TollFare class</h5>
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
