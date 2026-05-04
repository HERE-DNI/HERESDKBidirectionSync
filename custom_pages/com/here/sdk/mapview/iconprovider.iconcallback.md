---
title: "IconProvider.IconCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesticonprovider-iconcallback"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface IconProvider.IconCallback

Enclosing class:
[IconProvider](sdk-for-android-explore-api-reference-latesticonprovider "class in com.here.sdk.mapview")

<!-- -->

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public static interface IconProvider.IconCallback
Interface which is used as callback to pass back an image or error code after calling the createRoadShieldIcon() method.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onCreateIconReply](#onCreateIconReply(android.graphics.Bitmap,java.lang.String,com.here.sdk.mapview.IconProviderError))`(android.graphics.Bitmap bitmap, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` description, `[`IconProviderError`](sdk-for-android-explore-api-reference-latesticonprovidererror "enum class in com.here.sdk.mapview")` error)`

Called when the image was created successfully or an error has occurred

## Method Details

### onCreateIconReply

void onCreateIconReply(@Nullable android.graphics.Bitmap bitmap, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description, @Nullable [IconProviderError](sdk-for-android-explore-api-reference-latesticonprovidererror "enum class in com.here.sdk.mapview") error)

    Called when the image was created successfully or an error has occurred
Parameters:
    `bitmap` - The created icon or `null` if an error occurred. Note that the resulting resolution of the image may differ from the width and height constraints because the aspect ratio is kept.

    `description` - An English description of the created icon. For example, "Federal Highway" for the road shield icon with the `RouteType.LEVEL_1_ROAD` in Brazil. Empty string if an error occurred.

    `error` - Error code if icon creation failed.
