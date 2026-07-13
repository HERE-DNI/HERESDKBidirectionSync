---
title: "EVSearchError enum - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evsearcherror"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVSearchError.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVSearchError-enum-sidebar.html">

<div>

# <span class="kind-enum">EVSearchError</span> enum

</div>

<div class="section desc markdown">

Specifies possible errors that `EVSearchEngine` may report.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Values

<span class="name">emptyIds</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
Empty list of IDs passed.

<span class="name">invalidId</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
At least one empty or invalid ID passed.

<span class="name">badRequest</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
Something wrong or missing in the request.

<span class="name">parsingError</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
EVCP3 backend returns result with unexpected json schema.

<span class="name">internalError</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
Generic internal error.

<span class="name">serverUnreachable</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
EVCP3 server is unreachable.

<span class="name">httpError</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
A general network request error.

<span class="name">authenticationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
EVCP3 operation is not authenticated. Check your credentials.

<span class="name">exceededUsageLimit</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
Credentials exceeded the allowed requests limit.

<span class="name">timedOut</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
The request timed out.

<span class="name">offline</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
The device has no internet connection.

<span class="name">operationCancelled</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
The request was cancelled (usually by the user).

<span class="name">proxyAuthenticationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
Proxy is not authenticated. Check your proxy credentials.

<span class="name">proxyServerUnreachable</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
Proxy server unreachable.

<span class="name">noResultsFound</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
No results found.

<span class="name">operationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>  
Search operation failed due to some reason.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-evsearcherror-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evsearcherror-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evsearcherror-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-evsearcherror-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evsearcherror-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-evsearcherror-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-search-evsearcherror-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-evsearcherror">EVSearchError</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
