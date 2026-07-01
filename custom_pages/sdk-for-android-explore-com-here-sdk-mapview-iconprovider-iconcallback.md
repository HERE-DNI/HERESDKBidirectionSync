---
title: "IconProvider.IconCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-iconprovider-iconcallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[IconProvider](sdk-for-android-explore-com-here-sdk-mapview-iconprovider "class in com.here.sdk.mapview")

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public static interface
</span><span class="element-name type-name-label">IconProvider.IconCallback</span>

</div>

<div class="block">

Interface which is used as callback to pass back an image or error code
after calling the createRoadShieldIcon() method.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onCreateIconReply(android.graphics.Bitmap bitmap,
   String description,
   IconProviderError error)</code></pre></td>
  <td><div class="block">
  Called when the image was created successfully or an error has occurred
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="onCreateIconReply(android.graphics.Bitmap,java.lang.String,com.here.sdk.mapview.IconProviderError)"
    class="section detail">

    ### onCreateIconReply

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onCreateIconReply</span><span class="parameters">(@Nullable
    android.graphics.Bitmap bitmap, @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> description,
    @Nullable
    [IconProviderError](sdk-for-android-explore-com-here-sdk-mapview-iconprovidererror "enum class in com.here.sdk.mapview") error)</span>

    </div>

    <div class="block">

    Called when the image was created successfully or an error has
    occurred

    </div>

    Parameters:  
    `bitmap` - The created icon or `null` if an error occurred. Note
    that the resulting resolution of the image may differ from the width
    and height constraints because the aspect ratio is kept.

    `description` - An English description of the created icon. For
    example, "Federal Highway" for the road shield icon with the
    `RouteType.LEVEL_1_ROAD` in Brazil. Empty string if an error
    occurred.

    `error` - Error code if icon creation failed.

    </div>

  </div>

</div>

