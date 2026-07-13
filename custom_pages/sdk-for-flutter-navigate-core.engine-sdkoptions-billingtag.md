---
title: "billingTag property - SDKOptions class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-sdkoptions-billingtag"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- billingTag.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">billingTag</span> property

</div>

<div class="section multi-line-signature">

String? <span class="name">billingTag</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Internal to HERE SDK. DO NOT USE THIS YET.

**Warning:** This is a placeholder and under developement. We will announce its availability in our changelog once it is ready for use.

A parameter to set a billing tag to track your HERE platform usage across the various HERE services your application may contact. For more information on the billing tag, see our <a href="https://www.here.com/docs/bundle/cost-management-developer-guide/page/topics/tutorial-billing-tags.html">cost management guide</a>. The tag needs to follow the format as described in the guide or it will be ignored. The parameter defaults to `null`, which also means that the tag is ignored for all requests.

**Note:** The billing tag is optional, but when set, it can help you to understand how often your app uses certain services, for example, the number of hits to our HERE backend routing services. For more details on tracking such details, please consult the *cost management guide* or get in touch with the HERE billing team.

</div>

## Implementation

``` dart
String? billingTag;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
