---
title: "PostActionListener constructor - PostActionListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-postactionlistener-postactionlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PostActionListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/PostActionListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">PostActionListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">PostActionListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onPostActionsLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onPostActionsLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-postaction-class">PostAction</a></span>\></span></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive post action notifications.

</div>

## Implementation

``` dart
factory PostActionListener(
  void Function(List<PostAction>) onPostActionsLambda,

) => PostActionListener$Lambdas(
  onPostActionsLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
