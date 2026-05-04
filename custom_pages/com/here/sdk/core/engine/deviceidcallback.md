---
title: "DeviceIdCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestdeviceidcallback"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface DeviceIdCallback

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface DeviceIdCallback
This method will be called on the main thread when [`SDKNativeEngine.getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)`](sdk-for-android-explore-api-reference-latestsdknativeengine#getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)) has been completed.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onDeviceIdCallbackCompleted](#onDeviceIdCallbackCompleted(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` deviceId)`

This method will be called on the main thread when [`SDKNativeEngine.getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)`](sdk-for-android-explore-api-reference-latestsdknativeengine#getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)) has been completed.

## Method Details

### onDeviceIdCallbackCompleted

void onDeviceIdCallbackCompleted(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) deviceId)

    This method will be called on the main thread when [`SDKNativeEngine.getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)`](sdk-for-android-explore-api-reference-latestsdknativeengine#getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)) has been completed.
Parameters:
    `deviceId` -

    Represents a deviceId, a unique identifier assigned to the device for this application.
