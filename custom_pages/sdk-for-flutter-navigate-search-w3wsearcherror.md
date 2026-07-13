---
title: "W3WSearchError enum - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-w3wsearcherror"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/W3WSearchError-enum-sidebar.html">

<div>

# <span class="kind-enum">W3WSearchError</span> enum

</div>

<div class="section desc markdown">

Specifies possible errors that may result from a w3w search query.

</div>

## Values

<span class="name">badWords</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
Invalid or non-existent 3 word address.

<span class="name">badLanguage</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
Bad parameter `language`.

<span class="name">missingWords</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
Missing parameter: a required words parameter was missing.

<span class="name">parsingError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
W3W backend return result with unexpected json schema. This is not expected to happen. Try updating to the newest version of the SDK. If the problem persists, please report a bug in the SDK.

<span class="name">internalError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
Generic internal error.

<span class="name">serverUnreachable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
What3Words server is unreachable.

<span class="name">httpError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
A general network request error.

<span class="name">authenticationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
What3Words operation is not authenticated. Check your credentials.

<span class="name">exceededUsageLimit</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
Credentials exceeded the allowed requests limit.

<span class="name">timedOut</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
The request timed out.

<span class="name">offline</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
The device has no internet connection.

<span class="name">operationCancelled</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
The request was cancelled (usually by the user).

<span class="name">proxyAuthenticationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
Proxy is not authenticated. Check your proxy credentials.

<span class="name">proxyServerUnreachable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
Proxy server unreachable.

<span class="name">unknown</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>  
Unknown error, that was not introduced by HERE SDK, but exists on W3W backend.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearcherror-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearcherror-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearcherror-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearcherror-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearcherror-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearcherror-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-search-w3wsearcherror-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

