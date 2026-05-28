---
title: "confirmHEREPrivacyNoticeException method"
slug: "sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- confirmHEREPrivacyNoticeException.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationengine-class</li>
<li class="self-crumb">confirmHEREPrivacyNoticeException method</li>
</ol>
<div class="self-name">confirmHEREPrivacyNoticeException</div>
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
<div class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>confirmHEREPrivacyNoticeException method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-location-confirmationstatus
confirmHEREPrivacyNoticeException(<wbr/>)

      <div class="features">override</div>
</section>
<section class="desc markdown">
<p>On Android devices by calling this method, the application developer confirms that they have received an
exceptional permission from HERE in written form to <strong>not</strong> include a reference to the HERE
Privacy Notice. As a result, the <code>LocationEngine</code> will not collect characteristic
information about the nearby mobile and Wi-Fi network signals. However, the engine will still
be fully functional and will deliver location updates when the exception can be confirmed.</p>
<p><strong>Note:</strong> This call should not involve user interaction and should be executed silently
by the application before starting the <code>LocationEngine</code>.</p>
<p>The permission for exceptional use will be verified asynchronously using your HERE SDK
credentials. A missing permission will cause the <code>LocationEngine</code> to stop, and
<code>LocationEngineStatus.PRIVACY_NOTICE_UNCONFIRMED</code> will be delivered to the
<code>LocationStatusListener</code>.</p>
<p>Returns:</p>
<ul>
<li>A confirmation action status. Valid values are defined in /sdk-for-flutter-navigate-location-confirmationstatus.</li>
<li>A first-time call may result in <code>ConfirmationStatus.PENDING</code>. Ensure that the
<code>LocationStatusListener</code> is used to get notified if permission remains unconfirmed.</li>
</ul>
<p>On iOS devices this method does nothing and /sdk-for-flutter-navigate-location-confirmationstatus is returned.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ConfirmationStatus confirmHEREPrivacyNoticeException() =&gt;
    _location.confirmHEREPrivacyNoticeException();</code></pre>
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
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationengine-class</li>
<li class="self-crumb">confirmHEREPrivacyNoticeException method</li>
</ol>
<h5>LocationEngine class</h5>
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
`
}</HTMLBlock>
